# aa-api/databse/model.py

from .db import db


class Bus(db.Document):
    number_plate = db.StringField(required=True, unique=True)
    manufacturer = db.StringField(required=True)
    model = db.StringField(required=True)
    year = db.IntField(required=True)
    capcity = db.IntField(required=True)
