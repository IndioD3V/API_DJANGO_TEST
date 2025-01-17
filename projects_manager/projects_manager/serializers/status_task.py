from projects_manager.models.status_task import StatusTask
from projects_manager.models.status_tables import SCHEMA_STATUS_TABLES
from projects_manager.libs.common import get_field_schema
from .serializer_master import SerializerMaster

class StatusTaskSerializer(SerializerMaster):
    class Meta:
        model = StatusTask
        fields = get_field_schema(SCHEMA_STATUS_TABLES) + SerializerMaster.new_field
