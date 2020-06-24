# Casting Agency API

This is the API for the casting agency.

### General Specifications
- Models will include at least…
    - Two classes with primary keys at at least two attributes each
    - Optional but encouraged] One-to-many or many-to-many relationships between classes
- Endpoints will include at least…
    - Two GET requests
    - One POST request
    - One PATCH request
    - One DELETE request
- Roles will include at least…
    - Two roles with different permissions
    - Permissions specified for all endpoints
- Tests will include at least….
    - One test for success behavior of each endpoint
    - One test for error behavior of each endpoint
    - At least two tests of RBAC for each role

### Casting Agency Specifications
- The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

- Models:
    - Movies with attributes title and release date
    - Actors with attributes name, age and gender
- Endpoints:
    - GET /actors and /movies
    - DELETE /actors/ and /movies/
    - POST /actors and /movies and
    - PATCH /actors/ and /movies/
- Roles:
    - Casting Assistant
        - Can view actors and movies
    - Casting Director
        - All permissions a Casting Assistant has and…
        - Add or delete an actor from the database
        - Modify actors or movies
    - Executive Producer
        - All permissions a Casting Director has and…
        - Add or delete a movie from the database
- Tests:
    - One test for success behavior of each endpoint
    - One test for error behavior of each endpoint
    - At least two tests of RBAC for each role
    
## Getting Started

### Installing Dependencies

#### Python 3.7

The project was created with python-3.7.7. The Heroku server is also using python-3.7.7 via the file runtime.txt.

#### Virtual Enviornment

Information on setting up virtual environments with PIP can be done here [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

This project was used [conda](https://docs.conda.io/en/latest/miniconda.html) as the python package manager, however, PIP was still used to install packages. The conda virtual environment was called fsnd_proj5, though the name shouldn't really matter.

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we use to handle cross origin requests from the frontend server.

## Running the server

Make sure you are working in the virtual environment.

To run the server, execute:

NOTE: If you are on windows `setup.sh` would not work, however it you use Git Bash, it recognizes some Linux commands.
You can copy the contents in the `setup.sh` and execute it in Git Bash. Alternatively, you can just set all of the
environment variable names the way Windows sets them.

```bash
source setup.sh
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Running `setup.sh` sets some environment variables used by the app, including the JWT access tokens.

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the this file to find the application.

You can run this API locally at the default `http://127.0.0.1:5000/`

## Unit Tests

Run the unit tests
```
dropdb fsndcapstone_test
createdb fsndcapstone_test
psql fsndcapstone_test < database/fsndcapstone_test_db.psql
python test_app.py
```

NOTE: The Auth0 access tokens expire after a certain amount of time. You can look at `unit_test_results.txt` to see 
that the unit test did pass all tests at one point in time when all of the Auth0 access tokens were active.

You can also use Postman collection to test the endpoints with this file `fsnd-capstone.postman_collection.json`. However,
these tests are not comprehensive. It does include the different roles but just `GET`, no `POST`, `PATCH`, `DELETE`. The results
of the Postman collection is here `fsnd-capstone.postman_test_run.json`.

## Deployment

The app is deployed on Heroku [link](https://heroku-fsndcap-app-cilsya.herokuapp.com/).

## API Reference

### Getting Started

- Base URL: [link](https://heroku-fsndcap-app-cilsya.herokuapp.com/)
- Authentication: This app has 3 users. Each has his own token which are provided in `setup.sh` file. Details about each user privilege are provided below.

### Endpoints

- GET '/actors'
- GET '/movies'
- POST '/actors'
- POST '/movies'
- PATCH '/actors/<int:id>'
- PATCH '/movies/<int:id>'
- DELETE '/actors/<int:id>'
- DELETE '/movies/<int:id>'