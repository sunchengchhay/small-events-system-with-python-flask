from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_jwt_extended import JWTManager

from app.customs.authorizations import authorizations

api = Api(version='1.0', title='API Document',
          description='API for System Design', authorizations=authorizations)
db = SQLAlchemy()
jwt = JWTManager()
