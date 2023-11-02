from flask_restx import Namespace, Resource
from flask import request
from flask_jwt_extended import jwt_required

from app.apis.models import *
from app.models import (
    SysMenu,
    SysSubMenu,
    SysRight,
    SysProfile,
    SysProfileAccessRight,
)
from app.extensions import db

ns = Namespace("System Access and Privilege Settings",
               description="System Access and Privilege Settings endpoint", path='/settings')

ns.decorators = [jwt_required()]


@ns.route('/Menus')
class Menus(Resource):
    @ns.expect(sys_menu_model_post)
    @ns.marshal_with(sys_menu_model)
    @ns.doc(security="jsonWebToken")
    def post(self):
        """Create an Menu item"""
        data = request.json or ns.payload
        menu = SysMenu(**data)

        db.session.add(menu)
        db.session.commit()
        return menu, 201

    @ns.marshal_list_with(sys_menu_model)
    @ns.doc(security="jsonWebToken")
    def get(self):
        """Get all Menu items"""
        return SysMenu.query.all()


@ns.route('/Menus/<int:id>')
class Menu(Resource):
    @ns.marshal_with(sys_menu_model)
    @ns.doc(security="jsonWebToken")
    def get(self, id):
        """Get a Menu item by ID"""
        menu = SysMenu.query.get_or_404(id)
        return menu, 201

    @ns.expect(sys_menu_model_put)
    @ns.marshal_with(sys_menu_model)
    @ns.doc(security="jsonWebToken")
    def put(self, id):
        """Update an Organization by ID"""
        data = ns.payload or request.json
        menu = SysMenu.query.get_or_404(id)
        menu.name_latin = data["name_latin"]
        menu.order = data["order"]
        menu.updated_by = data["updated_by"]
        menu.updated_at = data["updated_at"]

        db.session.commit()

        return {"msg": "updated successfully"}, 200

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        """Delete an Organization by ID"""
        menu = SysMenu.query.get_or_404(id)
        db.session.delete(menu)
        db.session.commit()
        return {"msg": "deleted successfully"}, 204


@ns.route('/sub_menus')
class SubMenus(Resource):
    @ns.expect(sys_sub_menu_model_post)
    @ns.marshal_with(sys_sub_menu_model)
    @ns.doc(security="jsonWebToken")
    def post(self):
        """Create an Sub Menu item"""
        data = request.json or ns.payload
        sub_menu = SysSubMenu(**data)

        db.session.add(sub_menu)
        db.session.commit()
        return sub_menu, 201

    @ns.marshal_list_with(sys_sub_menu_model)
    @ns.doc(security="jsonWebToken")
    def get(self):
        """Get all Sub Menu items"""
        return SysSubMenu.query.all()


@ns.route('/sub_menus/<int:id>')
class SubMenu(Resource):
    @ns.marshal_with(sys_sub_menu_model)
    @ns.doc(security="jsonWebToken")
    def get(self, id):
        """Get a Sub Menu item by ID"""
        sub_menu = SysSubMenu.query.get_or_404(id)
        return sub_menu, 201

    @ns.expect(sys_sub_menu_model_put)
    @ns.marshal_with(sys_sub_menu_model)
    @ns.doc(security="jsonWebToken")
    def put(self, id):
        """Update an Sub Menu Item by ID"""
        data = ns.payload or request.json
        sub_menu = SysSubMenu.query.get_or_404(id)
        sub_menu.name_latin = data["name_latin"]
        sub_menu.sys_menu_id = data["sys_menu_id"]
        sub_menu.order = data["order"]
        sub_menu.endpoint = data["endpoint"]
        sub_menu.updated_by = data["updated_by"]
        sub_menu.updated_at = data["updated_at"]

        db.session.commit()

        return {"msg": "updated successfully"}, 200

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        """Delete an Sub Menu Item by ID"""
        sub_menu = SysSubMenu.query.get_or_404(id)
        db.session.delete(sub_menu)
        db.session.commit()
        return {"msg": "deleted successfully"}, 204


@ns.route('/rights')
class Rights(Resource):
    @ns.expect(sys_right_model_post)
    @ns.marshal_with(sys_right_model)
    @ns.doc(security="jsonWebToken")
    def post(self):
        """Create an Right item"""
        data = request.json or ns.payload
        right = SysRight(**data)

        db.session.add(right)
        db.session.commit()
        return right, 201

    @ns.marshal_list_with(sys_right_model)
    @ns.doc(security="jsonWebToken")
    def get(self):
        """Get all Right items"""
        return SysRight.query.all()


@ns.route('/rights/<int:id>')
class Right(Resource):
    @ns.marshal_with(sys_right_model)
    @ns.doc(security="jsonWebToken")
    def get(self, id):
        """Get a Right item by ID"""
        right = SysRight.query.get_or_404(id)
        return right, 201

    @ns.expect(sys_right_model_put)
    @ns.marshal_with(sys_right_model)
    @ns.doc(security="jsonWebToken")
    def put(self, id):
        """Update an Right item by ID"""
        data = ns.payload or request.json
        right = SysRight.query.get_or_404(id)
        right.acronym = data["acronym"]
        right.description = data["description"]
        right.updated_by = data["updated_by"]
        right.updated_at = data["updated_at"]

        db.session.commit()

        return {"msg": "updated successfully"}, 200

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        """Delete an Right item by ID"""
        right = SysRight.query.get_or_404(id)
        db.session.delete(right)
        db.session.commit()
        return {"msg": "deleted successfully"}, 204


@ns.route('/profiles')
class Profiles(Resource):
    @ns.expect(sys_profile_model_post)
    @ns.marshal_with(sys_profile_model)
    @ns.doc(security="jsonWebToken")
    def post(self):
        """Create an Profile Role Item"""
        data = request.json or ns.payload
        profile = SysProfile(**data)

        db.session.add(profile)
        db.session.commit()
        return profile, 201

    @ns.marshal_list_with(sys_profile_model)
    @ns.doc(security="jsonWebToken")
    def get(self):
        """Get all Profile Role Items"""
        return SysProfile.query.all()


@ns.route('/profiles/<int:id>')
class Profile(Resource):
    @ns.marshal_with(sys_profile_model)
    @ns.doc(security="jsonWebToken")
    def get(self, id):
        """Get a profile role item by ID"""
        profile = SysProfile.query.get_or_404(id)
        return profile, 201

    @ns.expect(sys_profile_model_put)
    @ns.doc(security="jsonWebToken")
    def put(self, id):
        """Update a profile role item by ID"""
        data = ns.payload or request.json
        profile = SysProfile.query.get_or_404(id)
        profile.acronym = data["acronym"]
        profile.name_latin = data["name_latin"]
        profile.updated_by = data["updated_by"]
        profile.updated_at = data["updated_at"]

        db.session.commit()

        return {"msg": "updated successfully"}, 200

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        """Delete a profile role item by ID"""
        profile = SysProfile.query.get_or_404(id)
        db.session.delete(profile)
        db.session.commit()
        return {"msg": "deleted successfully"}, 204


@ns.route('/profile_access_rights')
class ProfileAccessRights(Resource):
    @ns.expect(sys_profile_access_right_model_post)
    @ns.marshal_with(sys_profile_access_right_model)
    @ns.doc(security="jsonWebToken")
    def post(self):
        """Create an Profile Access Right Item"""
        data = request.json or ns.payload
        profile = SysProfileAccessRight(**data)

        db.session.add(profile)
        db.session.commit()
        return profile, 201

    @ns.marshal_list_with(sys_profile_access_right_model)
    @ns.doc(security="jsonWebToken")
    def get(self):
        """Get all Profile Access Right Items"""
        return SysProfileAccessRight.query.all()


@ns.route('/profile_access_rights/<int:id>')
class ProfileAccessRight(Resource):
    @ns.marshal_with(sys_profile_access_right_model)
    @ns.doc(security="jsonWebToken")
    def get(self, id):
        """Get a profile Access Right item by ID"""
        profile = SysProfileAccessRight.query.get_or_404(id)
        return profile, 201

    @ns.expect(sys_profile_access_right_model_put)
    @ns.doc(security="jsonWebToken")
    def put(self, id):
        """Update a Profile Access Right item by ID"""
        data = ns.payload or request.json
        profile = SysProfileAccessRight.query.get_or_404(id)

        profile.sys_profile_id = data["sys_profile_id"]
        profile.sys_sub_menu_id = data["sys_sub_menu_id"]
        profile.sys_right_id = data["sys_right_id"]
        profile.updated_by = data["updated_by"]
        profile.updated_at = data["updated_at"]
        db.session.commit()

        return {"msg": "updated successfully"}, 200

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        """Delete a Profile Access Right Item by ID"""
        profile = SysProfileAccessRight.query.get_or_404(id)
        db.session.delete(profile)
        db.session.commit()
        return {"msg": "deleted successfully"}, 204
