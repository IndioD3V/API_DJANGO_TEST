from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from projects_manager.models.developer import Developer
from projects_manager.serializers.developer import DeveloperSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class DeveloperViewSet(ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    
    permission_classes = [IsAuthenticated]  # Requer autenticação
    
    @action(detail=True, methods=['delete'])
    def delete_developer(self, request, pk=None):
        developer = self.get_object()
        # Atualizar as tasks associadas para não ter um developer
        developer.tasks.update(developer=None)
        # Agora você pode excluir o developer
        developer.delete()
        return Response(status=204)
