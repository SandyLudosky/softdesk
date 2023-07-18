from django.urls import path
from .views import contributor_list, contributor_detail

urlpatterns = [
    path('contributors/', contributor_list),
    path('contributors/<int:pk>/', contributor_detail),
]