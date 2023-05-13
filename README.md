# yt-pandas-dlp
What if yt-dlp could create spreadsheets

@ozaki: Hello i've been using a website to backup my playlist but it doens't seems to work anymore
so i wanted to go on using yt-dlp for this. the backup i used was looking like this and i want to achieve something similar
i don't care about some columns like the description and it would be cool to have it in a csv / excel /table format else a json will do the trick

@IsaacKoi I'm also trying to produce a spreadsheet with columns like channel, webpage URL, upload date, title and description.
I've previously used an online tool but for various reasons would now prefer to use yt-dlp (basically, to have a bit more control and ability to tweak things).
I've managed to output the data I want from yt-dlp as both csv files and as json filesy fiddly issues importing some of the data into spreadsheets.

# How to use it

* Find some youtube channel, say `https://www.youtube.com/@MickWest/videos`
* Create folder `MickWest` to store `*.json` and `*.srt`
* `cd MickWest`
* `yt-dlp --write-info-json --write-auto-sub --sub-langs en --write-subs --convert-subs srt --skip-download https://www.youtube.com/@MickWest/videos`
* `cd ..`
* `python json2xlsx.py MickWest`
* Find two generated files, `MickWest/Mick West - Videos.cvs`  and `MickWest/Mick West - Videos.xlsx`

# Known issues

* I need to actually test it in Windows
* `=HYPERLINK` may be broken (or not?)
