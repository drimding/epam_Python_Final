from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.models.home_model import Home


class HomeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Home
        exclude = ('id', 'user_id')
        load_instance = True
        include_fk = True
