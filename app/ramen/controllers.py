from flask import Blueprint
from flask_restful import Api, Resource
from app.models import get_session, Store

ramen_api = Blueprint('ramen_api', __name__)
api = Api(ramen_api)


@api.resource('')
class RamenList(Resource):

    def get(self):
        with get_session() as session:
            store_list = session.query(Store).all()
            result = [store.row2dict() for store in store_list]
        return {'aa': result}
