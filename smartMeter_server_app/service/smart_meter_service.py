from sqlalchemy.exc import IntegrityError

from smartMeter_server_app import db
from smartMeter_server_app.service.main_service import MainService


class SmartMeterService(MainService):
    def add(self, home_id):
        try:
            self.home_id = home_id
            db.session.add(self)
            db.session.commit()
        except IntegrityError as e:
            return {"message": str(e.orig)}, 400
        return 201