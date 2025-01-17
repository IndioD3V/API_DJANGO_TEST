from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from projects_manager.models.project_technology import ProjectTechnology
from projects_manager.serializers.project_technology import ProjectTechnologySerializer


class ProjectTechnologyViewSet(ModelViewSet):
    queryset = ProjectTechnology.objects.all()
    serializer_class = ProjectTechnologySerializer
    
    permission_classes = [IsAuthenticated]  # Requer autenticação
