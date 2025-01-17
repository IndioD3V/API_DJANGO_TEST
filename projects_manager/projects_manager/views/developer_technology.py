from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from projects_manager.models.developer_technology import DeveloperTechnology
from projects_manager.serializers.developer_technology import DeveloperTechnologySerializer


class DeveloperTechnologyViewSet(ModelViewSet):
    queryset = DeveloperTechnology.objects.all()
    serializer_class = DeveloperTechnologySerializer
    
    permission_classes = [IsAuthenticated]  # Requer autenticação
