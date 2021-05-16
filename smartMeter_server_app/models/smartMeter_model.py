import uuid

from smartMeter_server_app import db
from smartMeter_server_app.models.ApplianceMetaData_model import ApplianceMetaData


class SmartMeter(db.Model):
    __tablename__ = 'smart_meters'

    id = db.Column(db.Integer, primary_key=True)
    meter_name = db.Column(db.String(50), nullable=False)
    uuid = db.Column(db.String(36), unique=True, nullable=False)
    home_id = db.Column(db.Integer, db.ForeignKey('homes.id'), nullable=False)
    meta_data = db.relationship('ApplianceMetaData', backref='smart_meters', lazy='subquery', cascade="all, delete-orphan")

    def __init__(self, meter_name, home_id):
        self.meter_name = meter_name
        self.uuid = str(uuid.uuid4())
        self.home_id = home_id
