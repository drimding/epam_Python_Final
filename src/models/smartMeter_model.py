import uuid

from src import db
from src.models.ApplianceMetaData_model import ApplianceMetaData
from src.service.smart_meter_service import SmartMeterService


class SmartMeter(db.Model, SmartMeterService):
    __tablename__ = 'smart_meters'
    __table_args__ = (db.UniqueConstraint('meter_name', 'home_id', name='unique_smart_meter'),)

    id = db.Column(db.Integer, primary_key=True)
    meter_name = db.Column(db.String(50), nullable=False)
    uuid = db.Column(db.String(36), unique=True, index=True)
    home_id = db.Column(db.Integer, db.ForeignKey('homes.id'), nullable=False)
    meta_data = db.relationship('ApplianceMetaData', backref='smart_meters', lazy='subquery', cascade="all, delete-orphan")

    def __init__(self, meter_name):
        self.meter_name = meter_name
        self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return f'SmartMeter({self.meter_name}, {self.uuid}, {self.home_id})'
