from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from marshmallow import ValidationError

from src import db
from src.models.home_model import Home
from src.models.smartMeter_model import SmartMeter
from src.schemas.smartMeter_schema import SmartMeterSchema


class SmartMeterApi(Resource):
    smart_meter_schema = SmartMeterSchema()

    def get(self, home_uuid=None, meter_uuid=None):
        home = Home.get_by_uuid(home_uuid)
        if not home:
            return "", 404
        if meter_uuid:
            smart_meter = SmartMeter.get_by_uuid(meter_uuid)
            return self.smart_meter_schema.dump(smart_meter), 200
        else:
            return self.smart_meter_schema.dump(home.smart_meters, many=True), 200

    def post(self, home_uuid=None):
        home = Home.get_by_uuid(home_uuid)
        if not home:
            return "", 404
        try:
            smart_meter = self.smart_meter_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        print(smart_meter)
        return self.smart_meter_schema.dump(smart_meter.add(home.id))

    def put(self):
        return "PUT", 200

    def delete(self, home_uuid=None, meter_uuid=None):
        home = Home.get_by_uuid(home_uuid)
        if not home:
            return "", 404
        return SmartMeter.delete(meter_uuid)
