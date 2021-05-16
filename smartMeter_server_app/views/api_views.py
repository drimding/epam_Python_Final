from smartMeter_server_app import api
from smartMeter_server_app.rest.home_api import Home

api.add_resource(Home, '/api/v1.0/home/', '/api/v1.0/home/<uuid>', strict_slashes=False)
