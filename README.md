# Book-Recommender-System
Its is a project to recommend similar books to the client, using different techniques.

1. Popularity Based 
2. Collaborative Filtering
3. Hybrid Recommender


# Local Setup
- Clone the project
- Run ` bash local_setup.sh`

# Local Development Run
- `bash local_run.sh` It will start the flask app in `development`. Suited for local development

# Replit run
- Go to shell and run
    `pip install --upgrade poetry`
- Click on `main.py` and click button run
- Sample project is at https://replit.com/@thejeshgn/flask-template-app
- The web app will be availabe at https://flask-template-app.thejeshgn.repl.co
- Format https://<replname>.<username>.repl.co

# Folder Structure

- `db_directory` has all the csv files regarding the books used in the project.
- `application` is where our application code is
- `local_setup.sh` set up the virtualenv inside a local `.env` folder. Uses `pyproject.toml` and `poetry` to setup the project
- `local_run.sh`  Used to run the flask application in development mode
- `static` - default `static` files folder. It serves at '/static' path. More about it is [here](https://flask.palletsprojects.com/en/2.0.x/tutorial/static/).
- `templates` - Default flask templates folder
- `pickle` - Holds binary files after processing in the `book-recommender.ipynb` file, used in the application


