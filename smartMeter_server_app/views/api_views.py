from smartMeter_server_app import api
from smartMeter_server_app.rest.home_api import HomeApi

api.add_resource(HomeApi, '/api/v1.0/home/', '/api/v1.0/home/<uuid>', strict_slashes=False)
