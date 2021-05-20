import datetime

import uuid

from src import db


class ApplianceMetaData(db.Model):
    __tablename__ = 'ApplianceMetaData'

    id = db.Column(db.Integer, primary_key=True)
    meter_value = db.Column(db.Integer(), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow, index=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False)
    smart_meters_id = db.Column(db.Integer, db.ForeignKey('smart_meters.id'), nullable=False)

    def __init__(self, meter_value, smart_meters_id):
        self.meter_value = meter_value
        self.uuid = str(uuid.uuid4())
        self.smart_meters_id = smart_meters_id
