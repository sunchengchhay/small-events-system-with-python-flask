from app.extensions import api
from flask_restx import fields

from app.customs.cambodia_datetime import current_time_cambodia

time_cambodia = current_time_cambodia()

# Define a model
login_model = api.model('Login', {
    "username": fields.String(required=True, description='Username'),
    "password": fields.String(required=True, description='Password')
})

register_model = api.model('Register', {
    "username": fields.String(required=True, description='Login name'),
    "password": fields.String(required=True, description='Password'),
    "sys_profile_id": fields.Integer(required=True, description='Sys profile'),
    "name_latin": fields.String(required=True, description='Name latin'),
    "name_khmer": fields.String(required=True, description='Name khmer'),
    "sys_position_id": fields.Integer(required=False, description='Position'),
    "sys_department_id": fields.Integer(required=False, description='Department'),
    "sys_organization_id": fields.Integer(required=False, description='Organization'),
    "phone": fields.String(required=True, description='Phone'),
    "email": fields.String(required=True, description='Email'),
    "sys_nationality_id": fields.Integer(required=True, description='Nationality'),
    "created_at": fields.DateTime(default=time_cambodia, description='Created at'),
    "created_by": fields.Integer(required=True, description='Created by'),
    "updated_at": fields.DateTime(default=time_cambodia, description='Updated at'),
    "updated_by": fields.Integer(required=True, description='Updated by'),
    "sys_gender_id": fields.Integer(required=True, description='Gender')
})
