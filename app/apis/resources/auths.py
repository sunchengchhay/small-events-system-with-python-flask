from flask_restx import Namespace, Resource
from flask import request, jsonify
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                jwt_required,
                                current_user,
                                get_jwt_identity, get_jwt)
from werkzeug.security import generate_password_hash, check_password_hash

from app.apis.models import register_model, login_model
from app.extensions import db
from app.models import SysPerson, SysUser

ns = Namespace("Authenthication", description="Authenthication endpoints")


@ns.route("/register")
class Register(Resource):

    @jwt_required()
    @ns.doc(security="jsonWebToken")
    @ns.expect(register_model)
    @ns.marshal_with(register_model)
    def post(self):
        """Register a new user"""
        data = ns.payload or request.json
        person = SysPerson(name_latin=data["name_latin"], name_khmer=data["name_khmer"], sys_position_id=data["sys_position_id"], department_id=data["sys_department_id"], sys_organization_id=data["sys_organization_id"], phone=data["phone"],
                           email=data["email"], sys_nationality_id=data["sys_nationality_id"], created_at=data["created_at"], created_by=data["created_by"], updated_at=data["updated_at"], updated_by=data["updated_by"], sys_gender_id=data["sys_gender_id"])
        db.session.add(person)
        db.session.commit()
        last_person = SysPerson.query.order_by(SysPerson.id.desc()).first()
        print(last_person.id)
        user = SysUser(login_name=data["username"], password=generate_password_hash(data["password"]), status=1, sys_profile_id=data["sys_profile_id"],
                       sys_person_id=last_person.id, created_at=data["created_at"], created_by=data["created_by"], updated_at=data["updated_at"], updated_by=data["updated_by"])
        db.session.add(user)
        db.session.commit()
        return person, 201


@ns.route("/login")
class Login(Resource):
    @ns.expect(login_model)
    def post(self):
        """Login a user"""
        data = ns.payload or request.json
        user = SysUser.query.filter_by(username=data["username"]).first()

        if user:
            if check_password_hash(user.password, data["password"]):
                access_token = create_access_token(identity=user.username)

                return {"access_token": access_token,
                        "user_id ":  user.id,
                        "message": "login sucessfully"
                        }, 200
            else:
                return {"message": "Wrong password"}, 401
        else:
            return {"message": "User not found"}, 404


@ns.route("/protected")
class Protected(Resource):
    @jwt_required()
    @ns.doc(security="jsonWebToken")
    def get(self):
        return get_jwt()
