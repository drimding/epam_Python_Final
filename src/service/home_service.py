from sqlalchemy.exc import IntegrityError

from src import db

from src.service.main_service import MainService


class HomeService(MainService):
    @classmethod
    def get_all(cls, user):
        return db.session.query(cls).filter_by(user_id=user.id).all()

    def add(self, user):
        try:
            self.user_id = user.id
            db.session.add(self)
            db.session.commit()
        except IntegrityError as e:
            return {"message": str(e.orig)}, 400
        return self

    def set(self):
        db.session.add(self)
        db.session.commit()
        return self
