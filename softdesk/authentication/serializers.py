from django.contrib.auth.models import Group
from .models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    # password1 =
    class Meta:

        model = User
        fields = ['age', 'can_be_shared', 'can_be_contacted', 'url', 'username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data["password1"] != data["password2"]:
            serializers.ValidationError("password do not match")
        if data['age'] < 15:
            data['can_be_contacted'] = False
            data['can_be_shared'] = False
        return data


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']