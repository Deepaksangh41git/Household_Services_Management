import sre_parse
from flask_restful import Api,Resource,fields, marshal_with,reqparse
from flask_security import auth_required
from back_end.models import db,Service,ServiceRequest

api=Api(prefix='/api')

parser=reqparse.RequestParser() #convert data to dict 

#marshal
service_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'base_price': fields.Float,
    'duration': fields.Integer,
    'is_active': fields.Boolean,
}
service_request_fields = {
    'id': fields.Integer,
    'customer_id': fields.Integer,
    'service_id': fields.Integer,
    'professional_id': fields.Integer,
    'request_date': fields.DateTime,
    'status': fields.String,
    'remarks': fields.String,
    'location': fields.String,
    'completion_date': fields.DateTime,
}

class Services_List(Resource):
    @auth_required()
    @marshal_with(service_fields)

    def get(self):
        all_services=Service.query.all()
        return all_services
    def post(self):
        args=parser.parse_args()
        service=Service(**args)
        db.session.add(service)
        db.session.commit()
        return {"message":"Service Created"},200
    

api.add_resource(Services_List,'/service')