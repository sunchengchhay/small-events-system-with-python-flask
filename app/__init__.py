from flask import Flask

from app.config import Config
from app.extensions import db, api, jwt
from app.apis import api
from app.customs import jwt_identity


def create_app():

    app = Flask(__name__)
    # config
    config = Config()
    app.config.from_object(config)

    # init extensions
    db.init_app(app)
    api.init_app(app)
    jwt.init_app(app)

    jwt_identity

    return app
