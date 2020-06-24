"""
Description:
Entry point of main app.

Notes:
- CORS used for cross origin resource sharing.
- Use @requires_auth decorator to setup permissions based on role of user.
- Database and authorization related code separated out into their own folder.
"""

# -------------------------- Imports (Start) ----------------------------------

import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from .database.models import setup_db, Actors, Movies
from .auth.auth import AuthError, requires_auth

# -------------------------- Imports (End) ------------------------------------

# -------------------------- Functions (Start) --------------------------------


def create_app(test_config=None):
    """
    Function used to create the main app.
    """

    # create and configure the FLASK app
    app = Flask(__name__)

    # Separated out the database setup.
    # This will abstract and allow to swap out different databases (i.e.
    # SQLLite3, Postgres, MySQL, etc...)
    setup_db(app)

    # To handle Cross Origin Resource Sharing (CORS).
    # https://flask-cors.readthedocs.io/en/latest/
    CORS(app)

    # -----------------------------

    @app.after_request
    def after_request(response):

        response.headers.add(
            "Access-Control-Allow-Headers",
            "Content-Type, Authorization")

        response.headers.add(
            "Access-Control-Allow-Methods",
            "GET,POST,DELETE,PATCH")

        return response

    # -------------------------------------------------------------------------
    # Setup endpoints
    # (Start)
    # -------------------------------------------------------------------------

    @app.route("/")
    def welcome():
        msg = "Casting Agency App"
        return jsonify(msg)
        
    @app.route("/headers")
    def headers():
        #if 'Authorization' in request.headers:
        #    abort(401)
        #return "DEBUG - /headers endpoint is working!"
        return request.headers['Authorization']

    @app.route("/login-results")
    def loginresults():
        msg = ("Login results page. You should now have access to '/actors',"
               "'/movies', depending on your persmission level.")
        return jsonify(msg)

    @app.route("/movies", methods=["GET"])
    @requires_auth(permission="get:movies")
    def get_Movies(payload):
        """
        Return all movies from database
        """
        movies = Movies.query.all()
        mov_format = [mov.format() for mov in movies]
        result = {
            "success": True,
            "Movies": mov_format
        }
        return jsonify(result)

    @app.route("/movies/<int:id>", methods=["DELETE"])
    @requires_auth(permission="delete:movies")
    def delete_Movies(payload, id):
        """
        Delete movie via id
        """
        try:
            mov = Movies.query.filter_by(id=id).one_or_none()
            mov.delete()
            return jsonify({
                "success": True
            })
        except Exception:
            abort(422)

    @app.route("/movies", methods=["POST"])
    @requires_auth(permission="post:movies")
    def insert_Movies(payload):
        """
        Insert movie information
        """
        body = request.get_json()
        try:
            movie = Movies(
                name=body["name"],
                length=body["length"],
                genre=body["genre"])
            actors = Actors.query.filter(
                Actors.id == body["actor_ID"]).one_or_none()
            movie.Actors = [actors]
            movie.insert()
            return jsonify({
                "success": True
            })
        except Exception:
            abort(404)

    @app.route("/movies/<int:id>", methods=["PATCH"])
    @requires_auth(permission="patch:movies")
    def update_Movies(payload, id):
        """
        Update a movie via id
        """
        movie = Movies.query.filter(Movies.id == id).one_or_none()
        if movie is None:
            abort(404)
        body = request.get_json()
        if "name" in body:
            movie.name = body["name"]
        if "length" in body:
            movie.age = body["length"]
        if "genre" in body:
            movie.email = body["genre"]
        movie.update()
        return jsonify({
            "success": True,
        })

    @app.route("/actors", methods=["GET"])
    @requires_auth(permission="get:actors")
    def get_Actors(payload):
        """
        Return all actors from database
        """
        actors = Actors.query.all()
        act_format = [act.format() for act in actors]
        result = {
            "success": True,
            "Actors": act_format
        }
        return jsonify(result)

    @app.route("/actors/<int:id>", methods=["DELETE"])
    @requires_auth(permission="delete:actors")
    def delete_Actors(payload, id):
        """
        Delete actor via id
        """
        try:
            act = Actors.query.filter_by(id=id).one_or_none()
            act.delete()
            return jsonify({
                "success": True
            })
        except Exception:
            abort(422)

    @app.route("/actors", methods=["POST"])
    @requires_auth(permission="post:actors")
    def insert_Actors(payload):
        """
        Insert actor information
        """
        body = request.get_json()
        try:
            actor = Actors(
                name=body["name"],
                age=body["age"],
                email=body["email"],
                salary=body["salary"])
            movies = Movies.query.filter(
                Movies.id == body["movie_ID"]).one_or_none()
            actor.movies = [movies]
            actor.insert()
            return jsonify({
                "success": True
            })
        except Exception:
            abort(404)

    @app.route("/actors/<int:id>", methods=["PATCH"])
    @requires_auth(permission="patch:actors")
    def update_Actors(payload, id):
        """
        Update an actor information via id
        """
        actor = Actors.query.filter(Actors.id == id).one_or_none()
        if actor is None:
            abort(404)
        body = request.get_json()
        if "name" in body:
            actor.name = body["name"]
        if "age" in body:
            actor.age = body["age"]
        if "email" in body:
            actor.email = body["email"]
        if "salary" in body:
            actor.salary = body["salary"]
        actor.update()
        return jsonify({
            "success": True,
        })

    # -------------------------------------------------------------------------
    # Setup endpoints
    # (End)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Error handling
    # (Start)
    # -------------------------------------------------------------------------

    @app.errorhandler(AuthError)
    def unauthorized(error):
        print(error.status_code)
        print(error.error)
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
        }), error.status_code

    @app.errorhandler(400)
    def Bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'messege': "Bad request"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'messege': "Not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'messege': "Unprocessable request"
        }), 422

    @app.errorhandler(500)
    def InternelError(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal server error"
        }), 500

    # -------------------------------------------------------------------------
    # Error handling
    # (End)
    # -------------------------------------------------------------------------

    return app

# NOTE: This app variable is visible to the module when it is imported
#       There is another app variable that is only in the scope of
#       create_app() function for the FLASK app.
app = create_app()

# -------------------------- Functions (End) ----------------------------------

# -------------------------- Auto-Execute (Start) -----------------------------

if __name__ == '__main__':
    app.run()

# -------------------------- Auto-Execute (End) -------------------------------
