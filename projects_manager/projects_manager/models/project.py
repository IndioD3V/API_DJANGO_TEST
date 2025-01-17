from django.db.models import Model, PROTECT
from .status_project import StatusProject
from projects_manager.libs.common import fields_contructor

SCHEMA_PROJECT = [

    {
        "field": "name",
        "type": "CharField",
        "max_length": 50,
        "null": False,
        "blank": False
    },
    {
        "field": "start_date",
        "type": "DateField"
    },
    {
        "field": "end_date",
        "type": "DateField"
    },
    {
        "field": "code",
        "type": "CharField",
        "null":False,
        "unique":True,
        "max_length": 50
    },
    {
        "field": "status",
        "type": "ForeignKey",
        "to":StatusProject,
        "on_delete": PROTECT
        
    }
]

class Project(Model):
    class Meta:
        db_table = 'project'

fields_contructor(SCHEMA_PROJECT, Project)

Project.add_to_class(
    "__str__", lambda self: self.code
)