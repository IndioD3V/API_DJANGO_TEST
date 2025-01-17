from .status_tables import StatusTables

class StatusProject(StatusTables):
    class Meta:
        db_table = 'status_project'