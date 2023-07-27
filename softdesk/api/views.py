from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsOwnerOrReadOnly
from .models import Contributor, Project, Issue, Comment
from .serializers import ContributorSerializer,  ProjectSerializer, \
    IssueSerializer, CommentSerializer


class ProjectList(APIView):
    """
    List all projects, or create a new project.
    """

    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.user.is_authenticated:
            serializer = ProjectSerializer(data=request.data)
            request.data.update({'author': request.user.id})

            if serializer.is_valid(raise_exception=True):
                project = serializer.save()
                contributor = Contributor.objects.create(user=request.user, role='A')
                project.contributors.add(contributor)
                project.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ContributorList(generics.ListCreateAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


class ContributorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


class IssueList(APIView):
    """
    List all issues, or create a new issue.
    """
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get(self, request, format=None):
        issues = Issue.objects.all()
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if self.request.user.is_authenticated:
            serializer = IssueSerializer(data=request.data)
            request.data.update({'author': self.request.user.id})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class IssueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class CommentList(APIView):
    """
    List all comments, or create a new comment.
    """
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if self.request.user.is_authenticated:
            serializer = CommentSerializer(data=request.data)
            request.data.update({'author': self.request.user.id})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
