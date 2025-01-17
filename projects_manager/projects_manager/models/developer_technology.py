# EXTERNAL
from django.db.models import Model, CASCADE

# INTERNAL
from .technology import Technology
from .developer import Developer
from projects_manager.libs.common import fields_contructor

SCHEMA_DEVELOPE_TECHNOLOGY = [
    {
        "field": "developer",
        "type": "ForeignKey",
        "to": Developer,
        "to_field": "id",
        "on_delete": CASCADE
    },
    {
        "field": "technology",
        "type": "ForeignKey",
        "to": Technology,
        "to_field": "id",
        "on_delete": CASCADE
    }
]

class DeveloperTechnology(Model):
    class Meta:
        db_table = 'developer_technology'

fields_contructor(SCHEMA_DEVELOPE_TECHNOLOGY, DeveloperTechnology)

DeveloperTechnology.add_to_class(
    "__str__", lambda self: self.name
)