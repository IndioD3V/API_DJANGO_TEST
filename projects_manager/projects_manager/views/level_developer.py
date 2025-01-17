from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from projects_manager.models.level_developer import LevelDeveloper
from projects_manager.serializers.level_developer import LevelDeveloperSerializer


class LevelDeveloperViewSet(ModelViewSet):
    queryset = LevelDeveloper.objects.all()
    serializer_class = LevelDeveloperSerializer
    
    permission_classes = [IsAuthenticated]  # Requer autenticação
