# Casting Agency API

This is the API for the casting agency.

# WARNING
[Heroku Deployment](https://heroku-fsndcap-app-cilsya.herokuapp.com/)
NO FRONTEND. Use [curl](https://curl.haxx.se/download.html) or [Postman](https://www.postman.com)

If you use Postman, to test the endpoints of the users, you have to use the tokens by going to 
`Authorization`, set Type to `Bearer Token` and putting in the token value in the `Token` field. NOTE:
the tokens have an expiration time. I believe the Heroku server also have an expiration limit.

Here are the tokens for the different roles (REMEMBER THERE IS A TIME EXPIRATION):

```Bash
export AccessToken_Producer=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpqUjN2TUVDNGR1RmtCTTRfbDcwcCJ9.eyJpc3MiOiJodHRwczovL2Rldi16OXZ0YnctZS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjNzdjYTdkNjZlMWMwYmY0NTUwMTE2IiwiYXVkIjoiQ2FzdGluZ0FuZ2VuY3lJZGVudGlmaWVyIiwiaWF0IjoxNTkzMDA5MTE2LCJleHAiOjE1OTMwOTU1MTYsImF6cCI6IllWNE9INjc4czBpeXhqQXdxeGVhbWczM1FpMjlXeklEIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.lLfTXCBFSNzjBh4hOYFXAYJV680S_-JJ74uxx-XmhLaGzw3r-u1Qwmeva0V19IpHa9dyrAkYBrZore_N9mq_1CDYXoaFMrmPAT1eGaEtcF-4WQ0dPfLFuaaFLkbOxW8qa29ltABsl3g7VYzufVNq-4oq7l7RgZWt7qXL0A2MHfFX6D2MtYiJWl_xLryikfnTk8P3wN1dBRAx1pz2w5axguBcuuepjX8DmDkAAIJhCxoKZQbSfuxt2BkU4A9lnYyVD8-_0a1_SsmlaB_XFmm1J8wSV_M0ZPPqjAo_jI7J9KjtkZYzCDkpj6sMBp27E9eYk27Zdeb-RkdEeZnb04KrAQ
export AccessToken_Director=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpqUjN2TUVDNGR1RmtCTTRfbDcwcCJ9.eyJpc3MiOiJodHRwczovL2Rldi16OXZ0YnctZS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjNjU0NTM3MDYxZWEwYzY3MDczZGQ4IiwiYXVkIjoiQ2FzdGluZ0FuZ2VuY3lJZGVudGlmaWVyIiwiaWF0IjoxNTkzMDEwNDE5LCJleHAiOjE1OTMwOTY4MTksImF6cCI6IllWNE9INjc4czBpeXhqQXdxeGVhbWczM1FpMjlXeklEIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.C3xXYaLiqW5ZZiIW0HFqnJluGB2OLPc4f63UA2wNAxUWTaNDq9mQQP_WX6_OFJULXwGL05rzfV39DGi8LFSZJZjpO3pEFtw8TQLXvZXdcm9lBPoGx63kGgyS0AduKn0i1IXV6UeYRkqqfXUEviRVFgA5N5caKzkTA9HMv0czMNT-dlj_lQ_ZvASXdn6KGx6LpgPvUYt8KsT7qkh65ThIFn9xd2HOsfkp2Z69H3dTj2IREgreO8uZi73rlgCF7Vz7AEz23IpU08lPZRLUX43WYgPeN2MOFYhfPxFELg2NvsUyJr_qR4ORUGUvDyBi99HyhreEM3e4ESLcDMrKbR8-eg
export AccessToken_Assistant=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpqUjN2TUVDNGR1RmtCTTRfbDcwcCJ9.eyJpc3MiOiJodHRwczovL2Rldi16OXZ0YnctZS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVmMzZhNjU2NzY5ZDgwMDEzMjQxN2U3IiwiYXVkIjoiQ2FzdGluZ0FuZ2VuY3lJZGVudGlmaWVyIiwiaWF0IjoxNTkzMDEwOTA2LCJleHAiOjE1OTMwOTczMDYsImF6cCI6IllWNE9INjc4czBpeXhqQXdxeGVhbWczM1FpMjlXeklEIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.rIuCWsDh3Ag7cSUwHaJ1_jEra1VcbDsUNq_p0tBhUx6M-JwueTKNZa_ckVRkGsfWSNA2MMWfKI6Txri1bDnLyoqf_87TU_prhXTTFFlYq85sE_PtAQcdVo38xljTQPFwckAPNLJtm9aieF4fRAUVbUhdlAXuvvF4OL8lXKPPv9RXJFwefBejKFfMWiLDQfMncb7b2UvOzWQ7bEA29va7tTqzrOZLc1IDTprbKBtzO8lL39dQqHsT969NpLECzxfotm5B9j9SiMEs1WHXITowMhYAKgaUIBwkCEmSb6Q2X8v6EDBE4CA0j3729zeUxMpcWKxY_6wgsZghBciiUBJ8GQ
```

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