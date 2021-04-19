from flask_restful import Resource


class Index_page(Resource):
    def get(self):
        return {"message": "OK"}
