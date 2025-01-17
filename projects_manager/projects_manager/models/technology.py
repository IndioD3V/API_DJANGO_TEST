from django.db.models import Model
from projects_manager.libs.common import fields_contructor

SCHEMA_TECHNOLOGY = [

    {
        "field": "name",
        "type": "CharField",
        "max_length": 50,
        "null": False,
        "blank": False
    },
    {
        "field": "alias",
        "type": "CharField",
        "max_length": 12,
        "unique":True,
        "null": False
    }
]

class Technology(Model):
    class Meta:
        db_table = 'technology'

fields_contructor(SCHEMA_TECHNOLOGY, Technology)

Technology.add_to_class(
    "__str__", lambda self: self.name
)
