import os
import sys
import glob
import json
import pandas as pd
from copy import deepcopy


def init(path):
    win = "win" if sys.platform.startswith("win") else None

    base = "http://files.afu.se/Downloads/Transcriptions/Videos"
    row = {
        "Channel": path,
        "Uploaded Date": "2019-06-24",
        "Video URL": "https://youtu.be/{id}",
        "Video Title": "",
        "Description": "",
        "Base URL": f"{base}/Vodcasts/{path}/{path} - ",
        "Divider": "_",
        "Youtube id": "",
        "End URL": " - transcript (automated).pdf",
        "Transcript Link": '=HYPERLINK(F{n}&D{n}&G{n}&H{n}&I{n}; "Transcript Link")',
    }
    return row, win


def to_date(s):
    # 20200213 -> 2020-02-13
    return f"{s[:4]}-{s[4:6]}-{s[6:]}"


def to_dict(fn):
    with open(fn, "r") as f:
        data = json.load(f)
    return data


def to_name(path, fn, ext="xlsx"):
    full = os.path.join(path, fn)
    return f"{full}.{ext}"


def get_row(initial, data):
    row = deepcopy(initial)
    row["Uploaded Date"] = to_date(data["upload_date"])
    row["Video URL"] = row["Video URL"].format(id=data["id"])
    row["Video Title"] = data["title"]
    row["Description"] = data["description"]
    row["Youtube id"] = data["id"]
    return row


def process(initial, win, path):
    jsons = dict()
    it = glob.glob(os.path.join(path, "*.json"))
    for fn in sorted(it):
        print("Processing:", fn)
        data = to_dict(fn)
        if playlist_index := data.get("playlist_index"):
            jsons[playlist_index] = get_row(initial, data)
        else:
            pref = data["title"]
    for_pandas = [jsons[key] for key in sorted(jsons)]
    for i, elem in enumerate(for_pandas, start=2):  # 1 is for header
        elem["Transcript Link"] = elem["Transcript Link"].format(n=i)
    df = pd.DataFrame(for_pandas)
    df.to_excel(to_name(path, pref), index=False, header=True)
    df.to_csv(
        to_name(path, pref, "cvs"),
        index=False,
        header=True,
        lineterminator="\r\n" if win else "\n",
    )


def main() -> int:
    path = sys.argv[1]
    row, win = init(path)
    process(row, win, path)
    return 0


if __name__ == "__main__":
    exit(main())
