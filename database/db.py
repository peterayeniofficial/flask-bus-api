# aa-api/databse/db.py

from flask_mongoengine import MongoEngine

db = MongoEngine()


def initialize_db(app):
    db.init_app(app)
