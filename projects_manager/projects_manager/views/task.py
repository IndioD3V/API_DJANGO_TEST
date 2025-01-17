from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from projects_manager.models.task import Task
from projects_manager.serializers.task import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    permission_classes = [IsAuthenticated]  # Requer autenticação
