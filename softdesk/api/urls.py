from django.urls import path
from .views import contributor_list, contributor_detail, project_list,\
    project_detail, issue_list, issue_detail


urlpatterns = [
    path('contributors/', contributor_list),
    path('contributors/<int:pk>/', contributor_detail),
    path('projects/', project_list),
    path('projects/<int:pk>/', project_detail),
    path('issues/', issue_list),
    path('issues/<int:pk>/', issue_detail),
]