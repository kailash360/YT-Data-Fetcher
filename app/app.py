from flask import Flask, request
from app.controller.controller import Controller

app = Flask(__name__)

controller = Controller(app)

@app.route("/")
def health_check():
    return "Server is happy and running"

@app.get("/search")
def search():
    return controller.search_video(request)
    