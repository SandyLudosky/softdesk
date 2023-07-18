from django.urls import path
from .views import ContributorList, ContributorDetail,  ProjectList, ProjectDetail,\
      IssueList, IssueDetail, CommentList, CommentDetail


urlpatterns = [
    path('contributors/', ContributorList.as_view()),
    path('contributors/<int:pk>/', ContributorDetail.as_view()),
    path('projects/', ProjectList.as_view()),
    path('projects/<int:pk>/', ProjectDetail.as_view()),
    path('issues/', IssueList.as_view()),
    path('issues/<int:pk>/', IssueDetail.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
]

