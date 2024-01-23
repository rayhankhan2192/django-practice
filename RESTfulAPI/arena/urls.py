from django.urls import path
from .import views

urlpatterns = [
    path('details/', views.Teachers_Info, name='details/'),
    path('details/<int:primarykey>', views.Teachers_, name='details/'),
    path('info/', views.Tacher_create, name='info'),
]
