import os
import pathlib

from flask_swagger_ui import get_swaggerui_blueprint

BASE_DIR = pathlib.Path(__file__).parent


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:root@127.0.0.1:3306/develop'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY') or 'secret-key-goes-here'

    PROPAGATE_EXCEPTIONS = True
    #JWT_TOKEN_LOCATION = 'cookies'



