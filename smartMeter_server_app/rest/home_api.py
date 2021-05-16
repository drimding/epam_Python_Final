from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from marshmallow import ValidationError

from smartMeter_server_app import db
from smartMeter_server_app.schemas.home_schema import HomeSchema
from smartMeter_server_app.service.home_service import HomeService
from smartMeter_server_app.service.user_service import UserService


class Home(Resource):
    homes_schema = HomeSchema()

    @jwt_required()
    def get(self, uuid=None):
        if not uuid:
            return self.homes_schema.dump(HomeService.get_all(), many=True), 200
        return self.homes_schema.dump(HomeService.get_by_uuid(uuid)), 200

    @jwt_required()
    def post(self):
        try:
            home = self.homes_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        return HomeService.add(home)

    @jwt_required()
    def put(self, uuid=None):
        return "PUT", 201

    @jwt_required()
    def delete(self, uuid=None):
        return HomeService.delete(uuid)
