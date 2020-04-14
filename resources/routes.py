from .bus import BusesApi, BusApi


def initialize_routes(api):
    api.add_resource(BusesApi, '/api/buses')
    api.add_resource(BusApi, '/api/buses/<id>')
