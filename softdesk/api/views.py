from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Contributor, Project
from .serializers import ContributorSerializer,  ProjectSerializer


@csrf_exempt
def contributor_list(request):
    """
    List all contributors, or create a new contributor
    """
    if request.method == 'GET':
        contributors = Contributor.objects.all()
        serializer = ContributorSerializer(contributors, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ContributorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def contributor_detail(request, pk):
    """
    Retrieve or delete a contributor
    """
    try:
        contributor = Contributor.objects.get(pk=pk)
    except Contributor.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ContributorSerializer(Contributor)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        contributor.delete()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
def project_list(request):
    """
    List all projects, or create a new project.
    """
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)