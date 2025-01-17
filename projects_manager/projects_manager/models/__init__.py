
# TABLES STATUS
from projects_manager.models.status_developer import StatusDeveloper
from projects_manager.models.status_project import StatusProject
from projects_manager.models.status_task import StatusTask
from projects_manager.models.level_developer import LevelDeveloper
from projects_manager.models.status_tables import StatusTables, SCHEMA_STATUS_TABLES

# TABLES PRINCIPAL
from projects_manager.models.developer import Developer, SCHEMA_DEVELOPER
from projects_manager.models.technology import Technology, SCHEMA_TECHNOLOGY
from projects_manager.models.project import Project, SCHEMA_PROJECT
from projects_manager.models.task import Task, SCHEMA_TASK

# TABLES AUX
from projects_manager.models.developer_technology import DeveloperTechnology, SCHEMA_DEVELOPE_TECHNOLOGY
from projects_manager.models.project_technology import ProjectTechnology, SCHEMA_PROJECT_TECHNOLOGY
