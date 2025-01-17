from projects_manager.models.developer_technology import DeveloperTechnology
from projects_manager.models.developer import Developer
from projects_manager.models.technology import Technology
from .serializer_master import SerializerMaster
from rest_framework.serializers import  SlugRelatedField


class DeveloperTechnologySerializer(SerializerMaster):
    developer = SlugRelatedField(
        queryset=Developer.objects.all(),
        slug_field="cpf"
    )
    technology = SlugRelatedField(
        queryset=Technology.objects.all(),
        slug_field="name"
    )
    
    class Meta:
        model = DeveloperTechnology
        fields = SerializerMaster.new_field + ['developer'] + ['technology']
        
    def create(self, validated_data):
        return DeveloperTechnology.objects.create(
            developer_id=validated_data.get("developer").id,
            technology_id=validated_data.get("technology").id
        )

    
    def get_developer(self, obj):
        return Developer.objects.filter(id=obj.developer_id).values_list('name').first()

    def get_technology(self, obj):
        return Technology.objects.filter(id=obj.technology_id).values_list('name').first()
