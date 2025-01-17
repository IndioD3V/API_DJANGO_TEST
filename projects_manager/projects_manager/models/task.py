from django.db.models import Model, CASCADE, PROTECT, SET_NULL
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from projects_manager.libs.common import fields_contructor
from .status_task import StatusTask
from .project import Project
from .developer import Developer
from .developer_technology import DeveloperTechnology
from .project_technology import ProjectTechnology

SCHEMA_TASK = [
    {
        "field": "hours",
        "type": "FloatField",
        "default": 0.0
    },
    {
        "field": "project",
        "type": "ForeignKey",
        "to": Project,
        "to_field": 'id',
        "on_delete": CASCADE
    },
    {
        "field": "developer",
        "type": "ForeignKey",
        "to": Developer,
        "to_field": 'id',
        "on_delete": SET_NULL,
        "null":True, 
        "blank":True
    },
    {
        "field": "status",
        "type": "ForeignKey",
        "to": StatusTask,
        "to_field": 'id',
        "on_delete": PROTECT
    },
    {
        "field": "description",
        "type": "CharField",
        "unique": True,
        "null": False,
        "default": "Default Description"
        
    }
]

class Task(Model):
    class Meta:
        db_table = 'task'
    
fields_contructor(SCHEMA_TASK, Task)
