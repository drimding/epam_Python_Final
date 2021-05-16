from flask import Flask, Blueprint
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy, get_debug_queries
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint

import config


#bp = Blueprint('auth', __name__)

app = Flask(__name__)
app.config.from_object(config.Config)
#app.register_blueprint(bp)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Smart Meter'
    }
)
app.register_blueprint(SWAGGER_BLUEPRINT)

login_manager = LoginManager()
login_manager.login_view = 'mainpage'
login_manager.init_app(app)


def sql_debug(response):
    queries = list(get_debug_queries())
    total_duration = 0.0
    for q in queries:
        total_duration += q.duration

    print('=' * 80)
    print(' SQL Queries - {0} Queries Executed in {1}ms'.format(len(queries), round(total_duration * 1000, 2)))
    print('=' * 80)

    return response


app.after_request(sql_debug)

from smartMeter_server_app.views import main, api_views
from smartMeter_server_app.models.user_model import User
from smartMeter_server_app.models.home_model import Home
from smartMeter_server_app.models.smartMeter_model import SmartMeter
from smartMeter_server_app.models.ApplianceMetaData_model import ApplianceMetaData
