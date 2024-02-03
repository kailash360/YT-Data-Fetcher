from job.job import run_job
from app.app import app
from dotenv import load_dotenv

load_dotenv()

def main():
    run_job()
    app.run(debug=True)

if __name__ == '__main__':
    main()