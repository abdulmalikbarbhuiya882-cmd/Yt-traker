import requests
import time
from datetime import datetime

API_KEY = "AIzaSyA33IN-WpDGSBOhMWVRBmQy1FBNJra37fU"
VIDEO_ID = "Tdy--VVODxI"

last_views = None

while True:
    try:
        url = (
            "https://www.googleapis.com/youtube/v3/videos"
            f"?part=statistics&id={VIDEO_ID}&key={API_KEY}"
        )

        response = requests.get(url, timeout=30)
        data = response.json()

        if "items" not in data:
            print("YouTube API Error:", data)
        else:
            views = int(data["items"][0]["statistics"]["viewCount"])

            if views != last_views:
                print(
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Views:",
                    views
                )
                last_views = views

    except Exception as e:
        print("Error fetching:", e)

    # Exactly 5 minutes after each fetch
    time.sleep(300)
