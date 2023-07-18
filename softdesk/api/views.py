from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Contributor
from .serializers import ContributorSerializer


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