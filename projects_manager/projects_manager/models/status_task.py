from .status_tables import StatusTables

class StatusTask(StatusTables):
    class Meta:
        db_table = 'status_task'