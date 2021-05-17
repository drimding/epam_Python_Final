from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from marshmallow import ValidationError

from smartMeter_server_app import db
from smartMeter_server_app.models.home_model import Home
from smartMeter_server_app.schemas.home_schema import HomeSchema
from smartMeter_server_app.schemas.user_schema import UserSchema
from smartMeter_server_app.service.user_service import UserService


class HomeApi(Resource):
    homes_schema = HomeSchema()
    user_schema = UserSchema()

    @jwt_required()
    def get(self, uuid=None):
        if not uuid:
            return self.homes_schema.dump(Home.get_all(UserService.get_current_user()), many=True), 200
        return self.homes_schema.dump(Home.get_by_uuid(uuid)), 200

    @jwt_required()
    def post(self):
        try:
            home = self.homes_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        return home.add(UserService.get_current_user())

    @jwt_required()
    def put(self, uuid=None):
        home_in_db = Home.get_by_uuid(uuid)
        if not home_in_db:
            return "", 404
        try:
            home_update = self.homes_schema.load(request.json, instance=home_in_db, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        return self.homes_schema.dump(home_update.set()), 200

    @jwt_required()
    def delete(self, uuid=None):
        return Home.delete(uuid)
