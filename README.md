# YouTube Video Categorizer

This script allows batch categorize videos from YouTube channels: It fetches all videos from a given channel URL, prefilters the videos and lets you manually go through all video titles to categorize them. It finally writes the result to a csv-file.

content of `ouput.csv`:
```
https://youtube.com/watch?v=1263nDNDeXc,2
https://youtube.com/watch?v=8bosaxelegs,2
https://youtube.com/watch?v=2KWrudRbgO8,2
https://youtube.com/watch?v=wZNVUMVIcJI,1
https://youtube.com/watch?v=ZIEo61Izt4s,3
...
```

## Setup
- pytube for fetching YouTube data

```
pip install -r requirements.txt
```

## Using the script

```
python categorize_manually.py
```

You may modify the categories and pre-filtering defined in the beginning of the script.
