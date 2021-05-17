from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError

from smartMeter_server_app import db

from smartMeter_server_app.service.main_service import MainService


class HomeService(MainService):
    @classmethod
    def get_all(cls, user):
        return db.session.query(cls).filter_by(user_id=user.id).all()

    def add(self, user):
        try:
            self.user_id = user.id
            print(self)
            db.session.add(self)
            db.session.commit()
        except IntegrityError as e:
            return {"message": str(e.orig)}, 400
        return 201

    def set(self):
        db.session.add(self)
        db.session.commit()
        return self
