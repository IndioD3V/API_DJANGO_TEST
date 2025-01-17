from .status_tables import StatusTables

class StatusDeveloper(StatusTables):
    class Meta:
        db_table = 'status_developer'