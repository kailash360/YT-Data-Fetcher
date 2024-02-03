from apscheduler.schedulers.background import BackgroundScheduler

class Scheduler:
    def __init__(self, job, seconds):
        self.scheduler = BackgroundScheduler(daemon=True)
        self.scheduler.add_job(job, "interval", seconds = seconds)
    
    def start_mining(self):
        self.scheduler.start()

