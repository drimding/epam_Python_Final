from flask import redirect, url_for

from src import api, jwt
from src.rest.auth_api import AuthRegister, AuthLogin, Logout
from src.rest.mainpage_api import MainPage, Signup, Personal


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return redirect(url_for('logout'))


api.add_resource(MainPage, '/', strict_slashes=False)
api.add_resource(Signup, '/signup', strict_slashes=False)
api.add_resource(AuthRegister, '/auth/register', strict_slashes=False)
api.add_resource(AuthLogin, '/auth/login', strict_slashes=False)
api.add_resource(Logout, '/auth/logout', strict_slashes=False)
api.add_resource(Personal, '/personal', strict_slashes=False)
