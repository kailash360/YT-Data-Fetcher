# YouTube Data Fetcher

A simple data fetcher for YouTube based on a fixed query value. The data is stored in a MongoDB database and the collection is indexed on the publishing date of the videos.

## How to run ?

1. Copy the contents of `.env.example` into a `.env` file in root of the project.
2. Add the values of the environment variables as necessary
3. Create a virtual environment and activate it
> python -m venv venv
4. Install the dependencies
> pip install requirements.txt
5. Start the server 
> python main.py