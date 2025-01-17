from projects_manager.models.project_technology import ProjectTechnology
from projects_manager.models.project import Project
from projects_manager.models.technology import Technology
from .serializer_master import SerializerMaster
from rest_framework.serializers import  SlugRelatedField


class ProjectTechnologySerializer(SerializerMaster):
    project = SlugRelatedField(
        queryset=Project.objects.all(),
        slug_field="code"
    )
    technology = SlugRelatedField(
        queryset=Technology.objects.all(),
        slug_field="name"
    )
    
    class Meta:
        model = ProjectTechnology
        fields = SerializerMaster.new_field + ['project'] + ['technology']
        
    def create(self, validated_data):
        return ProjectTechnology.objects.create(
            project_id=validated_data.get("project").id,
            technology_id=validated_data.get("technology").id
        )

    
    def get_developer(self, obj):
        return Project.objects.filter(id=obj.project_id).values_list('name').first()

    def get_technology(self, obj):
        return Technology.objects.filter(id=obj.technology_id).values_list('name').first()
