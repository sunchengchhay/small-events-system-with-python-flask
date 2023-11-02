from flask_restx import Namespace, Resource
from flask import request
from flask_jwt_extended import jwt_required

from app.models import EveEvent
from app.extensions import db
from app.apis.models import input_event_model, update_event_model, output_event_model
from app.customs.authorizations import authorizations


ns = Namespace("Event Managements",
               description="Event Management endpoints", path="/", authorizations=authorizations)

ns.decorators = [jwt_required()]


@ns.route("/events")
class Events(Resource):
    @ns.expect(input_event_model)
    @ns.doc(security="jsonWebToken")
    def post(self):
        """Create an Event"""
        data = ns.payload or request.json
        event = EveEvent(**data)
        if event:
            db.session.add(event)
            db.session.commit()
            return {"msg": "Create successfully"}, 201
        return {"msg": "invalid created"}, 401

    @ns.marshal_list_with(output_event_model)
    @ns.doc(security="jsonWebToken")
    def get(self):
        """Get all Events"""
        return EveEvent.query.all()


@ns.route('/events/<int:id>')
class event(Resource):
    @ns.doc(security="jsonWebToken")
    @ns.marshal_with(output_event_model, code=201)
    def get(self, id):
        """Get an Event by ID"""
        event = EveEvent.query.get_or_404(id)
        return event, 201

    @ns.expect(update_event_model)
    @ns.doc(security="jsonWebToken")
    def put(self, id):
        """Update an Event"""
        data = ns.payload or request.json
        event = EveEvent.query.get_or_404(id)
        event.name_latin = data["name_latin"]
        event.name_khmer = data["name_khmer"]
        event.description = data["description"]
        event.start_date = data["start_date"]
        event.end_date = data["end_date"]
        event.photo_url = data["photo_url"]
        event.updated_by = data["updated_by"]
        event.updated_at = data["updated_at"]

        db.session.commit()

        return {"msg": "updated successfully"}, 200

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        """Delete an Event by ID"""
        event = EveEvent.query.get_or_404(id)
        db.session.delete(event)
        db.session.commit()
        return {"delete": "successfully"}, 204
