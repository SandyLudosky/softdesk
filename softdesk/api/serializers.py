from .models import Contributor
from rest_framework import serializers


class ContributorSerializer(serializers.ModelSerializer):
    """
    Contributor Serializer
    """
    def get_user(self, obj):
        """
        Display the user with his name
        """
        return f'{obj.user.first_name} {obj.user.last_name}'

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'role']