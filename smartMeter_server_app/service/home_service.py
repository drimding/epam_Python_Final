from sqlalchemy.exc import IntegrityError

from smartMeter_server_app import db
from smartMeter_server_app.models.home_model import Home
from smartMeter_server_app.models.user_model import User
from smartMeter_server_app.service.main_service import MainService
from smartMeter_server_app.service.user_service import UserService


class HomeService:

    @staticmethod
    def get_all():
        user = UserService.get_current_user()
        return db.session.query(Home).filter_by(user_id=user.id).all()

    @staticmethod
    def add(home: Home):
        try:
            home.user_id = UserService.get_current_user().id
            db.session.add(home)
            db.session.commit()
        except IntegrityError as e:
            return {"message": str(e.orig)}, 400
        return 201

    @staticmethod
    def get_by_uuid(uuid):
        return db.session.query(Home).filter_by(uuid=uuid).first()

    @staticmethod
    def set(uuid):
        pass

    @staticmethod
    def delete(uuid):
        home = HomeService.get_by_uuid(uuid)
        print(home)
        if not home:
            return "", 404
        db.session.delete(home)
        db.session.commit()
        return "", 204
