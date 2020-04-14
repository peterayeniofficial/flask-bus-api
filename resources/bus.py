from flask import Response, request
from database.models import Bus
from flask_restful import Resource


class BusesApi(Resource):
    def get(self):
        buses = Bus.objects().to_json()
        return Response(buses, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        bus = Bus(**body).save()
        return Response(bus, mimetype="application/json", status=200)
