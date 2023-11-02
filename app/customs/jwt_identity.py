from app.extensions import jwt, db
from app.models import SysUser, TokenBlocklist


# load user
@jwt.user_lookup_loader
def user_lookup_callback(jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return SysUser.query.filter_by(username=identity).one_or_none()


# error handlers
@jwt.unauthorized_loader
def missing_token_callback(error):
    return (
        {
            "message": "Request doesn't contain valid token",
            "error": "authorization_header",
        }
    ), 401


@jwt.token_in_blocklist_loader
def token_in_blocklist_callback(jwt_header, jwt_data):
    jti = jwt_data["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()
    return token is not None


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (
        {
            "message": "Signature verification failed",
            "error": "invalid_token"
        }
    ), 401


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return (
        {
            "message": "Token has expired",
            "error": "Token_expired"
        }
    ), 401


@jwt.needs_fresh_token_loader
def token_not_fresh_callback(jwt_header, jwt_data):
    return ({
        "description": "The token is not fresh.",
        "error": "fresh_token_required"
    }), 401


# additional claims
@jwt.additional_claims_loader
def make_additional_claims(identity):
    user = SysUser.query.filter_by(username=identity).first()
    role = user.sys_profile_id
    if role == 1:
        return {"is_admin": True, "user_id": user.id}
    return {"is_admin": False, "user_id": user.id}
