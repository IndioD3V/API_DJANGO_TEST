from django.db.models import Model
from projects_manager.libs.common import fields_contructor

SCHEMA_STATUS_TABLES = [

    {
        "field": "description",
        "type": "CharField",
        "max_length": 20,
        "unique":True,
        "null":False,
        "default": "Default Description"
    }
]

class StatusTables(Model):
    class Meta:
        abstract = True
    pass
fields_contructor(SCHEMA_STATUS_TABLES, StatusTables)
