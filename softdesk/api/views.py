from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly
from .models import Contributor, Project, Issue, Comment
from .serializers import ContributorSerializer,  ProjectSerializer, \
    IssueSerializer, CommentSerializer


class ProjectList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer): # read data from request
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
            serializer.save(contributors=self.request.user)
        else:
            serializer.save()


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


class IssueList(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class IssueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
