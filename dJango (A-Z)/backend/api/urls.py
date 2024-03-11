from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.api_home) # localhost:8080/api/
]
