from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from projects_manager.models.status_project import StatusProject
from projects_manager.serializers.status_project import StatusDeveloperSerializer


class StatusProjectViewSet(ModelViewSet):
    queryset = StatusProject.objects.all()
    serializer_class = StatusDeveloperSerializer
    
    permission_classes = [IsAuthenticated]  # Requer autenticação
