from flask_jwt_extended import jwt_required
from smartMeter_server_app import db


class MainService:

    @classmethod
    def get_by_uuid(cls, uuid) -> object:
        return db.session.query(cls).filter_by(uuid=uuid).first()

    @classmethod
    def delete(cls, uuid):
        obj = cls.get_by_uuid(uuid)
        if not obj:
            return "", 404
        db.session.delete(obj)
        db.session.commit()
        return "", 204