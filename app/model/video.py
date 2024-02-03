from mongoengine import *

class Video(Document):
    title = StringField()
    description = StringField()
    published_on = DateTimeField()
    thumbnail = URLField()
    url = URLField()
        