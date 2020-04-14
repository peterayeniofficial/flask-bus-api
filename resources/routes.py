from .bus import BusesApi


def initialize_routes(api):
    api.add_resource(BusesApi, '/api/buses')
