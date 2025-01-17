from rest_framework.serializers import SerializerMethodField, SlugRelatedField
from projects_manager.libs.common import get_field_schema
from projects_manager.models.developer import Developer, SCHEMA_DEVELOPER
from projects_manager.models.developer_technology import DeveloperTechnology
from projects_manager.models.status_developer import StatusDeveloper
from projects_manager.models.level_developer import LevelDeveloper
from projects_manager.models.technology import Technology
from .serializer_master import SerializerMaster


class DeveloperSerializer(SerializerMaster):
    tecnologias = SerializerMethodField()
    status = SlugRelatedField(
        queryset=StatusDeveloper.objects.all(),
        slug_field="description"
    )
    level = SlugRelatedField(
        queryset=LevelDeveloper.objects.all(),
        slug_field="description"
    )
    
    class Meta:
        model = Developer
        fields = get_field_schema(SCHEMA_DEVELOPER) + ['tecnologias'] + SerializerMaster.new_field

    def get_tecnologias(self, obj):
        tecnologias = DeveloperTechnology.objects.filter(developer_id=obj.id).values_list('technology_id', flat=True)
        tech_names = Technology.objects.filter(id__in=tecnologias).values_list('name', flat=True)
        return list(tech_names)
    
    def get_status(sefl, obj):
        status_id = Developer.objects.filter(id=obj.id).values_list('status', flat=True).first()
        return StatusDeveloper.objects.filter(id=status_id).values_list('description', flat=True).first()
    
    def get_level(self, obj):
        level_id = Developer.objects.filter(id=obj.id).values_list('level', flat=True).first()
        return LevelDeveloper.objects.filter(id=level_id).values_list('description', flat=True).first()
        
