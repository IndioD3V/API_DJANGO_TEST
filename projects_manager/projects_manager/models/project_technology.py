# EXTERNAL
from django.db.models import Model, CASCADE, PROTECT

# INTERNAL
from .project import Project
from .technology import Technology
from projects_manager.libs.common import fields_contructor

SCHEMA_PROJECT_TECHNOLOGY = [

    {
        "field": "project",
        "type": "ForeignKey",
        "to": Project,
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

class ProjectTechnology(Model):
    class Meta:
        db_table = 'project_technology'

fields_contructor(SCHEMA_PROJECT_TECHNOLOGY, ProjectTechnology)

ProjectTechnology.add_to_class(
    "__str__", lambda self: self.name
)
    
