import requests, os, datetime
from config.scheduler import Scheduler
from config.mongo import db
from constants import YOUTUBE_SEARCH_API_URL, YOUTUBE_SEARCH_QUERY, SCHEDULER_INERVAL

def get_last_video_time():
    last_video = list(db.Video.find().sort("published_on", -1).limit(1))
    
    if len(last_video) > 0:
        return last_video[0]["published_on"]
    else:
        return (datetime.datetime.now() - datetime.timedelta(days=7)).isoformat() + "Z"

def fetch_youtube_videos():
    try:
        last_video_time = get_last_video_time()
        
        query_params = {
            "part": "snippet",
            "q": YOUTUBE_SEARCH_QUERY, 
            "key": os.environ.get('YOUTUBE_API_KEY'),
            "type": "video",
            "publishedAfter": last_video_time
        }
        
        response = requests.get(YOUTUBE_SEARCH_API_URL, query_params)
        response = response.json()
        
        if "error" in response:
            raise RuntimeError(response["error"]["message"])
            
        items = response["items"]
        
        videos = []
        for item in items:
            data = item["snippet"]
            title = data["title"]
            description = data["description"]
            published_on = data["publishTime"]
            thumbnail = data["thumbnails"]["default"]["url"]
            url = item["id"]["videoId"]
            
            video = {
                "title": title,
                "description": description,
                "published_on": published_on,
                "thumbnail": thumbnail,
                "url": url
            }
            videos.append(video)
            
        db.Video.insert_many(videos)
    
    except Exception as e:
        print("Failed to fetch videos ", e.__str__())
    
def run_job():
    scheduler = Scheduler(fetch_youtube_videos, SCHEDULER_INERVAL);
    scheduler.start_mining()
    