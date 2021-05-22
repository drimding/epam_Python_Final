from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from marshmallow import ValidationError

from src import db
from src.models.home_model import Home
from src.schemas.home_schema import HomeSchema
from src.schemas.user_schema import UserSchema
from src.service.user_service import UserService


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
        response_home_added = home.add(UserService.get_current_user())
        return self.homes_schema.dump(response_home_added), 201

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
