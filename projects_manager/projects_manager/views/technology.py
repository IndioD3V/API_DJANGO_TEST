from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from projects_manager.models.technology import Technology
from projects_manager.serializers.technology import TechnologySerializer


class TechnologyViewSet(ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    
    permission_classes = [IsAuthenticated]  # Requer autenticação
