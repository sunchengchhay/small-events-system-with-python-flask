from .resources import auth_ns,user_ns,event_ns,user_info_ns,setting_ns
from app.extensions import api

# register namespace
api.add_namespace(auth_ns,path='/auth')
api.add_namespace(user_info_ns)
api.add_namespace(event_ns)
api.add_namespace(user_ns)
api.add_namespace(setting_ns)

