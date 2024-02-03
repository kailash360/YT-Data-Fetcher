from config.mongo import db
from constants import API_RESPONSE_VIDEO_COUNT
from utils.utils import parse_json

class Controller:
    def __init__(self, app):
        self.app = app
        
    def search_video(self, request):
        try:
            page = 0
            if "page" in request.args:
                page = int(request.args.get("page"))
                
            skip_count = page*API_RESPONSE_VIDEO_COUNT
            results = db.Video.find().sort({"published_on": -1}).skip(skip_count).limit(API_RESPONSE_VIDEO_COUNT)
            videos = [parse_json(v) for v in results]
            
            return { "success": True, "data": videos }
        except Exception as e:
            return { "success": False, "error": e.__str__()}