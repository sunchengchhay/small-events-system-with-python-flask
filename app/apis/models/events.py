from flask_restx import fields

from app.extensions import api
from app.customs.cambodia_datetime import current_time_cambodia, custom_datetime_cambodia

input_event_model = api.model(
    'EventInput',
    {
        "name_latin": fields.String(),
        "name_khmer": fields.String(),
        "description": fields.String(),
        "start_date": fields.DateTime(default=custom_datetime_cambodia('2023-12-09 7:00:00')),
        "end_date": fields.DateTime(default=custom_datetime_cambodia('2023-12-09 17:00:00')),
        "photo_url": fields.String(default="null"),
        "created_by": fields.Integer(default=1),
        "created_at": fields.DateTime(default=current_time_cambodia()),
        "updated_by": fields.Integer(default=1),
        "updated_at": fields.DateTime(default=current_time_cambodia()),
    }
)

output_event_model = api.model(
    'EventOutput',
    {
        "id": fields.Integer(),
        "name_latin": fields.String(),
        "name_khmer": fields.String(),
        "description": fields.String(),
        "start_date": fields.DateTime(default=custom_datetime_cambodia('2023-12-09 7:00:00')),
        "end_date": fields.DateTime(default=custom_datetime_cambodia('2023-12-09 17:00:00')),
        "photo_url": fields.String(default="null"),
        "created_by": fields.Integer(default=1),
        "created_at": fields.DateTime(default=current_time_cambodia()),
        "updated_by": fields.Integer(default=1),
        "updated_at": fields.DateTime(default=current_time_cambodia()),
    }
)

update_event_model = api.model(
    'EventUpdate',
    {
        "name_latin": fields.String(),
        "name_khmer": fields.String(),
        "description": fields.String(),
        "start_date": fields.DateTime(default=custom_datetime_cambodia('2023-12-09 7:00:00')),
        "end_date": fields.DateTime(default=custom_datetime_cambodia('2023-12-09 17:00:00')),
        "photo_url": fields.String(default="null"),
        "updated_by": fields.Integer(default=1),
        "updated_at": fields.DateTime(default=current_time_cambodia()),
    }
)
