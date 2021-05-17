import uuid

from smartMeter_server_app import db
from smartMeter_server_app.models.smartMeter_model import SmartMeter
from smartMeter_server_app.service.home_service import HomeService


class Home(db.Model, HomeService):
    __tablename__ = 'homes'
    __table_args__ = (db.UniqueConstraint('home_name', 'user_id', name='unique_component_commit'),)

    id = db.Column(db.Integer, primary_key=True)
    home_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    uuid = db.Column(db.String(36), unique=True)
    smart_meters = db.relationship('SmartMeter', backref='homes', lazy='subquery', cascade="all, delete-orphan")

    def __init__(self, home_name, address=None):
        self.uuid = str(uuid.uuid4())
        self.home_name = home_name
        self.address = address

    def __repr__(self):
        return f'Home {self.home_name}, {self.address}, {self.uuid}, {self.user_id}'




