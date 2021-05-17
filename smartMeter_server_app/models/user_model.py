from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from smartMeter_server_app import db
import uuid
from smartMeter_server_app.models.home_model import Home


class User(db.Model, UserMixin):
    """
    Create a users table
    Fields:
        id: the unique identifier of the user, primary key
        username:
        email:
        password:
        is_admin:
        uuid:
        homes:
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(254), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    uuid = db.Column(db.String(36), unique=True)
    homes = db.relationship('Home', backref='users', lazy='select', cascade="all, delete-orphan")

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.hash_password(password)
        self.uuid = str(uuid.uuid4())

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return self.uuid

    def __repr__(self):
        return f'User({self.username}, {self.email}, {self.uuid})'



