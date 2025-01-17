from projects_manager.models.task import Task, SCHEMA_TASK
from projects_manager.models.project import Project
from projects_manager.models.developer import Developer
from projects_manager.models.status_task import StatusTask
from projects_manager.models.project_technology import ProjectTechnology
from projects_manager.models.developer_technology import DeveloperTechnology
from projects_manager.models.project import Project
from projects_manager.models.developer import Developer
from projects_manager.models.task import Task
from .serializer_master import SerializerMaster
from projects_manager.libs.common import get_field_schema

from rest_framework.serializers import SlugRelatedField
from django.core.exceptions import ValidationError



class TaskSerializer(SerializerMaster):
    project = SlugRelatedField(
        queryset=Project.objects.all(),
        slug_field="code"
    )
    developer = SlugRelatedField(
        queryset=Developer.objects.all(),
        slug_field="cpf"
    )
    status = SlugRelatedField(
        queryset=StatusTask.objects.all(),
        slug_field="description"
    )
    
    class Meta:
        model = Task
        fields = get_field_schema(
            SCHEMA_TASK) + SerializerMaster.new_field + ['project'] + ['developer']
    
    def get_project(self, obj):
        return Project.objects.filter(
            id=obj.project_id).values_list('name').first()
    
    def get_developer(self, obj):
        return Developer.objects.filter(
            id=obj.developer_id).values_list('name').first()

    def validate(self, data):
        """
        Valida as condições do modelo Task, movendo a lógica de validação para o serializador.
        """
        
        error_tech = 'O desenvolvedor não possui as tecnologias necessárias para o projeto '
        error_time = "O total de horas alocadas excede as horas planejadas para o projeto "
        
        project = data.get('project')
        developer = data.get('developer')

        developer = Developer.objects.filter(
            cpf=developer).values('id', 'cpf').first()
        project = Project.objects.filter(
            code=project).values('id', 'start_date', 'end_date').first()

        project_technologies = {x for x in ProjectTechnology.objects.filter(
            project=project.get('id')).values_list("technology", flat=True)}
        developer_technologies = {x for x in  DeveloperTechnology.objects.filter(
            developer=developer.get('id')).values_list("technology", flat=True)}
        
        start_date = project.get('start_date')
        end_date = project.get('end_date')
        
        end_date = end_date if end_date else ''
        
        if end_date:
            time = (end_date - start_date).days * 24 
        else:
            time = True
            
        time =float(data.get('hours')) <=  time 
        
        have_tech = True if developer_technologies.intersection(
            project_technologies) else False
        
        if all([have_tech, time]):     
            return data
        else:
            if time is False and have_tech is False:
                raise ValidationError(error_tech + error_time)
            elif time is True and have_tech is False:
                raise ValidationError(error_tech)
            elif time is False and have_tech is True:
                raise ValidationError(error_time)

        
