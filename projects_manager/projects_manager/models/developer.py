from django.db.models import Model, PROTECT
from .status_developer import StatusDeveloper
from .level_developer import LevelDeveloper

from projects_manager.libs.common import fields_contructor


SCHEMA_DEVELOPER = [
    {
        "field": "name",
        "type": "CharField",
        "max_length": 120,
        "null": False
    },
    {
        "field": "cpf",
        "type": "CharField",
        "max_length": 12,
        "null":False,
        "unique":True
    },
    {
        "field": "level",
        "type": "ForeignKey",
        "to": LevelDeveloper,
        "to_field": 'id',
        
        "on_delete": PROTECT
    },
    {
        "field": "status",
        "type": "ForeignKey",
        "to": StatusDeveloper,
        "to_field": 'id',
        "on_delete": PROTECT
    }
]

class Developer(Model):
    class Meta:
        db_table = 'developer'

fields_contructor(SCHEMA_DEVELOPER, Developer)


Developer.add_to_class(
    "__str__", lambda self: self.cpf
)
