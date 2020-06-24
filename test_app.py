# -------------------------- Imports (Start) ----------------------------------

# Native modules
import json
import os
import unittest
from flask_sqlalchemy import SQLAlchemy

# Custom modules
from app import create_app
from models import setup_db, Actors, Movies

# -------------------------- Imports (End) ------------------------------------

# -------------------------- Classes (Start) ----------------------------------


class FSNDCapstoneTest(unittest.TestCase):
    """
    Description:
    Unit test for endpoints.

    NOTE: need to create database

    $dropdb fsndcapstone_test
    $createdb fsndcapstone_test
    $psql fsndcapstone_test < database/fsndcapstone_test_db.psql
    $python test_app.py

    # If you are running locally, you have to create the environment variable
    # in the setup.sh file for:
    #
    # export AccessToken_Producer=<ACCESS_TOKEN_VALUE>
    # export AccessToken_Director=<ACCESS_TOKEN_VALUE>
    # export AccessToken_Assistant=<ACCESS_TOKEN_VALUE>

    """

    def setUp(self):
        self.accesstoken_producer = os.environ['AccessToken_Producer']
        self.accesstoken_director = os.environ['AccessToken_Director']
        self.accesstoken_assistant = os.environ['AccessToken_Assistant']
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "fsndcapstone_test"
        self.user_name = "postgres"
        self.password = "postgres"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            self.user_name,
            self.password,
            'localhost:5432',
            self.database_name)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_Unauthorized_Permission_NO_HEADERS_get_Actors(self):
        res = self.client().get('/actors')
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(body['success'], False)

    def test_get_Actors(self):
        res = self.client().get('/actors', headers={
            "Authorization": 'bearer '+self.accesstoken_assistant})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)

    def test_404_wrong_endpoint_get_Actors(self):
        res = self.client().get('/actorss', headers={
            "Authorization": 'bearer '+self.accesstoken_assistant})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(body['success'], False)

    def test_get_Movies(self):
        res = self.client().get('/movies', headers={
            "Authorization": 'bearer '+self.accesstoken_assistant})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)

    def test_404_wrong_endpoint_get_Movies(self):
        res = self.client().get('/Movi', headers={
            "Authorization": 'bearer '+self.accesstoken_assistant})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(body['success'], False)

    def test_delete_Actor(self):
        res = self.client().delete('/actors/1', headers={
            "Authorization": 'bearer '+self.accesstoken_producer})
        body = json.loads(res.data)
        ques = Actors.query.filter_by(id=1).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)
        self.assertEqual(ques, None)

    def test_422_Wrong_ID_delete_Actor(self):
        res = self.client().delete('/actors/1000', headers={
            "Authorization": 'bearer '+self.accesstoken_producer})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(body['success'], False)

    def test_401_Unauthorized_Permission_delete_Actor(self):
        res = self.client().delete('/actors/1', headers={
            "Authorization": 'bearer '+self.accesstoken_assistant})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(body['success'], False)

    def test_delete_Movie(self):
        res = self.client().delete('movies/1', headers={
            "Authorization": 'bearer '+self.accesstoken_producer})
        body = json.loads(res.data)
        ques = Movies.query.filter_by(id=1).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)
        self.assertEqual(ques, None)

    def test_422_Wrong_ID_delete_Movies(self):
        res = self.client().delete('/movies/1000', headers={
            "Authorization": 'bearer '+self.accesstoken_producer})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(body['success'], False)

    def test_Unauthorized_Permission_delete_Movies(self):
        res = self.client().delete('/movies/1', headers={
            "Authorization": 'bearer '+self.accesstoken_assistant})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(body['success'], False)

    def test_create_Actor(self):
        res = self.client().post(
            '/actors',
            json={
                "name": "bob",
                "age": "10",
                "salary": "3000",
                "email": "bob@moviefilm.com",
                "movie_ID": "2"},
            headers={"Authorization": 'bearer '+self.accesstoken_director}
            )
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)

    def test_422_wrong_Movie_ID_create_Actor(self):
        res = self.client().post(
            '/actors',
            json={
                "name": "bob",
                "age": "10",
                "salary": "3000",
                "email": "bob@moviefilm.com",
                "movie_ID": "1000"},
            headers={"Authorization": 'bearer '+self.accesstoken_director}
            )
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(body['success'], False)

    def test_401_Unauthorized_Permission_create_Actor(self):
        res = self.client().post(
            '/actors',
            json={
                "name": "bob",
                "age": "10",
                "salary": "3000",
                "email": "bob@moviefilm.com",
                "movie_ID": "4"},
            headers={"Authorization": 'bearer '+self.accesstoken_assistant}
            )
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(body['success'], False)

    def test_create_Movie(self):
        res = self.client().post(
            '/movies',
            json={
                "name": "bob",
                "length": "10",
                "genre": "Action",
                "actor_ID": "3"},
            headers={"Authorization": 'bearer '+self.accesstoken_producer}
            )
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)

    def test_422_wrong_Actor_ID_create_Movie(self):
        res = self.client().post(
            '/movies',
            json={
                "name": "bob",
                "length": "10",
                "genre": "Action",
                "actor_ID": "10000"},
            headers={"Authorization": 'bearer '+self.accesstoken_producer}
            )
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(body['success'], False)

    def test_401_Unauthorized_Permission_create_Movie(self):
        res = self.client().post(
            '/movies',
            json={
                "name": "bob",
                "length": "10",
                "genre": "Action",
                "actor_ID": "10000"},
            headers={"Authorization": 'bearer '+self.accesstoken_assistant}
            )
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(body['success'], False)

    def test_update_Movies(self):
        res = self.client().patch(
            '/movies/2',
            json={
                "name": "bob",
                "length": "10",
                "genre": "Action"},
            headers={"Authorization": 'bearer '+self.accesstoken_producer}
            )
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)

    def test_404_wrong_ID_update_Movies(self):
        res = self.client().patch(
            '/movies/1000',
            json={
                "name": "bob",
                "length": "10",
                "genre": "Action"},
            headers={"Authorization": 'bearer '+self.accesstoken_producer}
            )
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(body['success'], False)

    def test_401_Unauthorized_Permission_update_Movies(self):
        res = self.client().patch(
            '/movies/1000',
            json={
                "name": "bob",
                "length": "10",
                "genre": "Action"},
            headers={"Authorization": 'bearer '+self.accesstoken_assistant}
            )
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(body['success'], False)

    def test_update_Actors(self):
        res = self.client().patch(
            '/actors/3',
            json={
                "name": "bob",
                "age": "10",
                "salary": "3000",
                "email": "bob@moviefilm.com"},
            headers={"Authorization": 'bearer '+self.accesstoken_producer}
            )
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)

    def test_404_wrong_ID_update_Actors(self):
        res = self.client().patch(
            '/actors/1000',
            json={
                "name": "bob",
                "age": "10",
                "salary": "3000",
                "email": "bob@moviefilm.com"},
            headers={"Authorization": 'bearer '+self.accesstoken_producer}
            )
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(body['success'], False)

# --------------------------- Classes (End) -----------------------------------

# -------------------------- Auto-Execute (Start) -----------------------------

if __name__ == "__main__":
    unittest.main()

# -------------------------- Auto-Execute (End) -------------------------------
