from smartMeter_server_app import db
from smartMeter_server_app.service.user_service import UserService


class MainService:

    @classmethod
    def get_by_uuid(cls, uuid):
        user = UserService.get_current_user()
        return db.session.query(cls).filter_by(user_id=user.id).all()
