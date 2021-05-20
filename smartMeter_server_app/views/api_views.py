from smartMeter_server_app import api
from smartMeter_server_app.rest.home_api import HomeApi
from smartMeter_server_app.rest.smartMeter_api import SmartMeterApi

api.add_resource(HomeApi, '/api/v1.0/home/', '/api/v1.0/home/<uuid>', strict_slashes=False)
api.add_resource(SmartMeterApi, '/api/v1.0/home/<home_uuid>/smartmeter', '/api/v1.0/home/<home_uuid>/smartmeter/<meter_uuid>', strict_slashes=False)
