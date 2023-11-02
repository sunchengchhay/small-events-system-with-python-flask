from .db import DB
from datetime import timedelta


class Config():
    DEBUG = True
    APP_NAME = "EVALUATE SYSTEM"
    SECRET_KEY = b'ZbCW2oMkb9_gBZ_WKhIl7mtsQVHX7vjSuev9d83ipoI='
    JWT_SECRET_KEY = 'fesystemjwttokenzin2nobodycanguessright'
    JWT_TOKEN_LOCATION = ["headers", "cookies"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_COOKIE_SECURE = True
    ERROR_404_HELP = False
    SQLALCHEMY_DATABASE_URI = DB().postgres_uri()
