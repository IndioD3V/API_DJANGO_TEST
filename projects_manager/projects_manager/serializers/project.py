from rest_framework.serializers import SerializerMethodField, SlugRelatedField
from projects_manager.models.project import Project, SCHEMA_PROJECT
from projects_manager.models.technology import Technology
from projects_manager.models.project_technology import ProjectTechnology
from projects_manager.models.status_project import StatusProject
from projects_manager.libs.common import get_field_schema
from .serializer_master import SerializerMaster


class ProjectSerializer(SerializerMaster):
    tecnologias = SerializerMethodField()
    status = SlugRelatedField(
        queryset=StatusProject.objects.all(),
        slug_field="description"
    )
    
    class Meta:
        model = Project
        fields = get_field_schema(SCHEMA_PROJECT) + ['tecnologias'] + SerializerMaster.new_field
    
    def get_tecnologias(self, obj):
        tecnologias = ProjectTechnology.objects.filter(project_id=obj.id).values_list('technology_id', flat=True)
        tech_names = Technology.objects.filter(id__in=tecnologias).values_list('name', flat=True)
        return list(tech_names)

    def get_status(sefl, obj):
        status_id = Project.objects.filter(id=obj.id).values_list('status', flat=True).first()
        return StatusProject.objects.filter(id=status_id).values_list('description', flat=True).first()
