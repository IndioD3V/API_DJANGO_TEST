from projects_manager.models.technology import Technology, SCHEMA_TECHNOLOGY
from projects_manager.libs.common import get_field_schema
from .serializer_master import SerializerMaster

class TechnologySerializer(SerializerMaster):
    class Meta:
        model = Technology
        fields = get_field_schema(SCHEMA_TECHNOLOGY) + SerializerMaster.new_field
