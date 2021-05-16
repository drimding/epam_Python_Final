from flask import render_template, make_response, redirect, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_login import login_required, current_user

from flask_restful import Resource


from smartMeter_server_app.service.user_service import UserService


class MainPage(Resource):
    def get(self):
        if current_user.is_authenticated:
            return redirect(url_for('personal'))
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('loginPage.html'), 200, headers)


class Signup(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('signup.html'), 200, headers)


class Personal(Resource):
    @jwt_required()
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), 200, headers)