from flask_restx import Namespace, Resource
from flask import request
from flask_jwt_extended import jwt_required

from app.apis.models import *

from app.models import (
    SysOrganization,
    SysNationality,
    SysPosition,
    SysDepartment,
    SysGender,
    SysPerson,
)
from app.extensions import db


ns = Namespace("User Infomations",
               description="User Informations endpoints", path='/')

ns.decorators = [jwt_required()]


# SysOrganization
@ns.route('/organizations')
class Organizations(Resource):

    @ns.expect(input_same_state_model)
    @ns.marshal_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def post(self):
        """Create an Organization"""
        data = request.json or ns.payload
        organization = SysOrganization(**data)

        db.session.add(organization)
        db.session.commit()
        return organization, 201

    @ns.marshal_list_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def get(self):
        """Get all Organizations"""
        return SysOrganization.query.all()


@ns.route('/organizations/<int:id>')
class Organization(Resource):

    @ns.marshal_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def get(self, id):
        """Get an Organization by ID"""
        organization = SysOrganization.query.get_or_404(id)
        return organization, 201

    @ns.expect(update_same_state_model)
    @ns.marshal_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def put(self, id):
        """Update an Organization by ID"""
        data = ns.payload or request.json
        organization = SysOrganization.query.get_or_404(id)
        organization.name_latin = data["name_latin"]
        organization.name_khmer = data["name_khmer"]
        organization.updated_by = data["updated_by"]
        organization.updated_at = data["updated_at"]

        return {"msg": "updated successfully"}, 200

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        """Delete an Organization by ID"""
        organization = SysOrganization.query.get_or_404(id)
        db.session.delete(organization)
        db.session.commit()
        return {"msg": "deleted successfully"}, 204


# SysNationality
@ns.route('/nationalities')
class Nationalities(Resource):
    @ns.expect(input_same_state_model)
    @ns.marshal_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def post(self):
        """Create an Nationality"""
        data = request.json or ns.payload
        nationality = SysNationality(**data)

        db.session.add(nationality)
        db.session.commit()
        return nationality, 201

    @ns.marshal_list_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def get(self):
        """Get all Nationalities"""
        return SysNationality.query.all()


@ns.route('/nationalities/<int:id>')
class Nationality(Resource):

    @ns.marshal_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def get(self, id):
        """Get an Nationality by ID"""
        nationality = SysNationality.query.get_or_404(id)
        return nationality, 201

    @ns.expect(update_same_state_model)
    @ns.marshal_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def put(self, id):
        """Update an Nationality by ID"""
        data = ns.payload or request.json
        nationality = SysNationality.query.get_or_404(id)
        nationality.name_latin = data["name_latin"]
        nationality.name_khmer = data["name_khmer"]
        nationality.updated_by = data["updated_by"]
        nationality.updated_at = data["updated_at"]

        return {"msg": "updated successfully"}, 200

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        """Delete an Nationality by ID"""
        nationality = SysNationality.query.get_or_404(id)
        db.session.delete(nationality)
        db.session.commit()
        return {"msg": "deleted successfully"}, 204


# SysPosition
@ns.route('/positions')
class Positions(Resource):

    @ns.expect(input_same_state_model)
    @ns.marshal_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def post(self):
        """Create an Position"""
        data = request.json or ns.payload
        position = SysPosition(**data)

        db.session.add(position)
        db.session.commit()
        return position, 201

    @ns.marshal_list_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def get(self):
        """Get all Positions"""
        return SysPosition.query.all()


@ns.route('/positions/<int:id>')
class Position(Resource):
    @ns.marshal_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def get(self, id):
        """Get an Position by ID"""
        position = SysPosition.query.get_or_404(id)
        return position, 201

    @ns.expect(update_same_state_model)
    @ns.marshal_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def put(self, id):
        """Update an Position by ID"""
        data = ns.payload or request.json
        position = SysPosition.query.get_or_404(id)
        position.name_latin = data["name_latin"]
        position.name_khmer = data["name_khmer"]
        position.updated_by = data["updated_by"]
        position.updated_at = data["updated_at"]

        return {"msg": "updated successfully"}, 200

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        """Delete an Position by ID"""
        position = SysPosition.query.get_or_404(id)
        db.session.delete(position)
        db.session.commit()
        return {"msg": "deleted successfully"}, 204


# SysDepartment
@ns.route('/departments')
class Departments(Resource):

    @ns.expect(input_same_state_model)
    @ns.marshal_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def post(self):
        """Create an Department"""
        data = request.json or ns.payload
        department = SysDepartment(**data)

        db.session.add(department)
        db.session.commit()
        return department, 201

    @ns.marshal_list_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def get(self):
        """Get all Departments"""
        return SysDepartment.query.all()


@ns.route('/departments/<int:id>')
class Department(Resource):
    @ns.marshal_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def get(self, id):
        """Get an Department by ID"""
        department = SysDepartment.query.get_or_404(id)
        return department, 201

    @ns.expect(update_same_state_model)
    @ns.doc(security="jsonWebToken")
    def put(self, id):
        """Update an Department by ID"""
        data = ns.payload or request.json
        department = SysDepartment.query.get_or_404(id)
        department.name_latin = data["name_latin"]
        department.name_khmer = data["name_khmer"]
        department.updated_by = data['updated_by']
        department.updated_at = data['updated_at']

        return {"msg": "updated successfully"}, 200

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        """Delete an Department by ID"""
        department = SysDepartment.query.get_or_404(id)
        db.session.delete(department)
        db.session.commit()
        return {"msg": "deleted successfully"}, 204


# SysGender
@ns.route('/genders')
class Genders(Resource):
    @ns.expect(input_same_state_model)
    @ns.marshal_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def post(self):
        """Create an Gender"""
        data = request.json or ns.payload
        gender = SysGender(**data)

        db.session.add(gender)
        db.session.commit()
        return gender, 201

    @ns.marshal_list_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def get(self):
        """Get all Genders"""
        return SysGender.query.all()


@ns.route('/genders/<int:id>')
class Gender(Resource):
    @ns.marshal_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def get(self, id):
        """Get an Gender by ID"""
        gender = SysGender.query.get_or_404(id)
        return gender, 201

    @ns.expect(update_same_state_model)
    @ns.marshal_with(output_same_state_model)
    @ns.doc(security="jsonWebToken")
    def put(self, id):
        """Update an Gender by ID"""
        data = ns.payload or request.json
        gender = SysGender.query.get_or_404(id)
        gender.name_latin = data["name_latin"]
        gender.name_khmer = data["name_khmer"]
        gender.updated_by = data["updated_by"]
        gender.updated_at = data["updated_at"]

        return {"msg": "updated successfully"}, 200

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        """Delete an Gender by ID"""
        gender = SysGender.query.get_or_404(id)
        db.session.delete(gender)
        db.session.commit()
        return {"msg": "deleted successfully"}, 204


@ns.route('/user_profiles')
class UserInfos(Resource):
    @ns.expect(sys_person_model_post)
    @ns.marshal_with(sys_person_model_get)
    @ns.doc(security="jsonWebToken")
    def post(self):
        """Create Person Infomation"""
        data = request.json or ns.payload
        sys_person = SysPerson(**data)

        db.session.add(sys_person)
        db.session.commit()
        return sys_person, 201

    @ns.marshal_list_with(sys_person_model_get)
    @ns.doc(security="jsonWebToken")
    def get(self):
        """Get all People Infomation"""
        return SysPerson.query.all()


@ns.route('/user_profiles/<int:id>')
class UserInfo(Resource):
    @ns.marshal_with(sys_person_model_get)
    @ns.doc(security="jsonWebToken")
    def get(self, id):
        """Get a User Infomation by ID"""
        sys_person = SysPerson.query.get_or_404(id)
        return sys_person, 201

    @ns.expect(sys_person_model_put)
    @ns.doc(security="jsonWebToken")
    def put(self, id):
        """Update a User Infomation by ID"""
        data = request.json or ns.payload
        sys_person = SysPerson.query.get_or_404(id)
        sys_person.name_latin = data['name_latin']
        sys_person.name_khmer = data['name_khmer']
        sys_person.photo_url = data['photo_url']
        sys_person.sys_gender_id = data['sys_gender_id']
        sys_person.sys_nationality_id = data['sys_nationality_id']
        sys_person.sys_organization_id = data['sys_organization_id']
        sys_person.sys_department_id = data['sys_department_id']
        sys_person.phone = data['phone']
        sys_person.email = data['email']
        sys_person.updated_by = data['updated_by']
        sys_person.updated_at = data['updated_at']

        return {"msg": "updated successfully"}, 200

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        """Delete a User Infomation by ID"""
        sys_person = SysPerson.query.get_or_404(id)
        db.session.delete(sys_person)
        db.session.commit()
        return {"msg": "deleted successfully"}, 204
