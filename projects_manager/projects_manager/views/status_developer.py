from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from projects_manager.models.status_developer import StatusDeveloper
from projects_manager.serializers.status_developer import StatusDeveloperSerializer


class StatusDeveloperViewSet(ModelViewSet):
    queryset = StatusDeveloper.objects.all()
    serializer_class = StatusDeveloperSerializer
    
    permission_classes = [IsAuthenticated]  # Requer autenticação
