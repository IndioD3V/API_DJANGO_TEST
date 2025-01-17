from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from projects_manager.models.developer import Developer
from projects_manager.serializers.developer import DeveloperSerializer


class DeveloperViewSet(ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    
    permission_classes = [IsAuthenticated]  # Requer autenticação
