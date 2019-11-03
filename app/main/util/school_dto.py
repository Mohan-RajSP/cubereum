from flask_restplus import fields, Api
from flask import Blueprint

school_blueprint = Blueprint('school_api', __name__)

school_swagger = Api(school_blueprint,
                            default='School',
                            default_label='This is the School Api service',
                            version='0.0.1',
                            title='School API with Python',
                            description='API for School API services',
                            ordered=True,
                         )

school = school_swagger.model('actionCreateRequest', {
    'district': fields.String(),
    'block': fields.String(),
    'cluster': fields.String(),
    'schoolid': fields.String(),
    'schoolname': fields.String(),
    'category': fields.String(),
    'gender': fields.String(),
    'medium_of_inst': fields.String(),
    'area': fields.String(),
    'pincode': fields.String(),
    'landmark': fields.String(),
    })

response = school_swagger.model('pythonBaseResponse', {
    'applicationCode': fields.Integer(),
    'code': fields.Integer(),
    'message': fields.String(),
    'status': fields.String()
    })

schoolBaseResponse = school_swagger.inherit('schoolBaseResponse', response, {
    'schoolDetails': fields.List(fields.Nested(school))
    })




