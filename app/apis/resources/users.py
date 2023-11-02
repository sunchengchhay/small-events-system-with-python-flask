from flask_restx import Namespace, Resource
from flask import request
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash

from app.apis.models import *
from app.models import *


ns = Namespace("Users Management",
               description="Users Management endpoints",
               path='/accounts')

ns.decorators = [jwt_required()]


@ns.route('/users')
class Users(Resource):

    @ns.expect(sys_user_model_post)
    @ns.marshal_with(sys_user_model)
    @ns.doc(security="jsonWebToken")
    def post(self):
        """Create Person Information"""
        data = ns.payload or request.json
        sys_user = SysUser(**data)
        sys_user.password = generate_password_hash(sys_user.password)
        db.session.add(sys_user)
        db.session.commit()
        return sys_user, 201

    @ns.marshal_list_with(sys_user_model)
    @ns.doc(security="jsonWebToken")
    def get(self):
        """Get People Information"""
        return SysUser.query.all()


@ns.route('/users/<int:id>')
class User(Resource):

    @ns.marshal_with(sys_person_model_get)
    @ns.doc(security="jsonWebToken")
    def get(self, id):
        """Get Person Information by ID"""
        sys_person = SysPerson.query.get_or_404(id)
        return sys_person, 201

    @ns.expect(sys_user_model_put)
    @ns.marshal_with(sys_user_model)
    @ns.doc(security="jsonWebToken")
    def put(self, id):
        """Update Person Information by ID"""
        data = ns.payload or request.json
        sys_user = SysUser.query.get_or_404(id)
        sys_user.username = data["username"]
        sys_user.password = generate_password_hash(data["password"])
        sys_user.status = data["status"]
        sys_user.last_login_at = data["last_login_at"]
        sys_user.sys_profile_id = data["sys_profile_id"]
        sys_user.sys_person_id = data["sys_person_id"]
        sys_user.updated_by = data["updated_by"]
        sys_user.updated_at = data["updated_at"]
        db.session.commit()

        return sys_user

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        """Delete Person Infomation item by ID"""
        sys_person = SysPerson.query.get_or_404(id)
        db.session.delete(sys_person)
        db.session.commit()
