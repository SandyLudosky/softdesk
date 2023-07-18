from .models import Contributor, Project
from rest_framework import serializers


class ContributorSerializer(serializers.ModelSerializer):
    """
    Contributor Serializer
    """
    class Meta:
        model = Contributor
        fields = ['id', 'user', 'role']


class ProjectSerializer(serializers.ModelSerializer):
    """
    Project Serializer
    """
    class Meta:
        model = Project
        fields = ['id',
                  'created_at',
                  'author',
                  'title',
                  'description',
                  'contributors']