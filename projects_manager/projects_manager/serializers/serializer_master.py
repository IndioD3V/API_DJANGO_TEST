from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.response import Response
from rest_framework import viewsets, status

class SerializerMaster(ModelSerializer):
    new_field = ['id']
    id = SerializerMethodField()
    def get_id(self, obj):
        return obj.id

    # METHOD UPDATE
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance

    # METHOD DELETE
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
