from django.urls import path
from .views import contributor_list, contributor_detail, ProjectList, ProjectDetail,\
      issue_list, issue_detail, comment_list, comment_detail


urlpatterns = [
    path('contributors/', contributor_list),
    path('contributors/<int:pk>/', contributor_detail),
    path('projects/', ProjectList.as_view()),
    path('projects/<int:pk>/', ProjectDetail.as_view()),
    path('issues/', issue_list),
    path('issues/<int:pk>/', issue_detail),
    path('comments/', issue_list),
    path('comments/<int:pk>/', issue_detail),
]

