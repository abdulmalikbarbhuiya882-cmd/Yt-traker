import requests
import time
from datetime import datetime

API_KEY = "AIzaSyDZzf2gSAqvmq_1fTUlL7YCVZ2LCjvSvh4"
VIDEO_ID = "wRgCUJx0gNo"

last_views = None

while True:
    try:
        url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={VIDEO_ID}&key={API_KEY}"
        r = requests.get(url).json()

        views = r['items'][0]['statistics']['viewCount']

        if views != last_views:
            print(datetime.now().strftime("%H:%M"), "Views:", views)
            last_views = views

    except:
        print("Error fetching")

    time.sleep(300)
