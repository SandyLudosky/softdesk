from .models import Contributor, Project, Issue
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


class IssueSerializer(serializers.ModelSerializer):
    """
    Issue Serializer
    """
    class Meta:
        model = Issue
        fields = ['id',
                  'title',
                  'project',
                  'description',
                  'author',
                  'assigned_user',
                  'tag', 'priority', 'status', 'created_at']
