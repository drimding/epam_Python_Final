from datetime import timedelta

from flask import request, redirect, url_for, make_response
from flask_restful import Resource
from marshmallow import ValidationError
from flask_jwt_extended import create_access_token, unset_jwt_cookies, set_access_cookies
from flask_login import login_user, login_required, logout_user, current_user
from src import db
from src.schemas.user_schema import UserSchema
from src.service.user_service import UserService


class AuthRegister(Resource):
    user_schema = UserSchema()

    def post(self):
        if request.json:
            try:
                user = self.user_schema.load(request.json, session=db.session)
                print(user)
                return UserService.add(user)
            except ValidationError as e:
                return {"message": str(e)}, 400
        else:
            try:
                user = self.user_schema.load({"username": request.form.get('username'),
                                              "password": request.form.get('password'),
                                              "email": request.form.get('email')},
                                             session=db.session)
            except ValidationError as e:
                return {"message": str(e)}, 400
            UserService.add(user)
            return redirect(url_for("mainpage"))


class AuthLogin(Resource):
    user_schema = UserSchema()

    def post(self):
        if request.json:
            json = request.json
            user = UserService.get_bu_username(json['username'])
            if not user or not user.check_password(json['password']):
                return "no authentication", 401
            jwt_token = create_access_token(identity=user.uuid, expires_delta=timedelta(hours=2))
            return {"jwt_token": "Bearer "+jwt_token}, 200
        else:
            if not request.form.get('password') or not request.form.get('username'):
                return "wrong input", 401
            user = UserService.get_bu_username(request.form.get('username'))
            if not user or not user.check_password(request.form.get('password')):
                return redirect(url_for('mainpage'))
            jwt_token = create_access_token(identity=user.uuid, expires_delta=timedelta(hours=2))
            login_user(user)
            headers = {'jwt_token': jwt_token}
            resp = make_response(redirect(url_for('personal')), 302, headers)
            r = redirect(url_for('personal'))
            set_access_cookies(resp, jwt_token)
            return resp


class Logout(Resource):
    @login_required
    def get(self):
        """User log-out logic."""
        logout_user()
        resp = make_response(redirect(url_for('mainpage')), 302)
        unset_jwt_cookies(resp)
        return resp
