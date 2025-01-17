from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from projects_manager.models.status_task import StatusTask
from projects_manager.serializers.status_task import StatusTaskSerializer


class StatusTaskViewSet(ModelViewSet):
    queryset = StatusTask.objects.all()
    serializer_class = StatusTaskSerializer
    
    permission_classes = [IsAuthenticated]  # Requer autenticação
