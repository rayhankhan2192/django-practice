from django.urls import path
from .import views, viewss, viewsss

urlpatterns = [
    path('details/', views.Teachers_Info, name='details/'),
    path('details/<int:primarykey>', views.Teachers_, name='details/'),
    path('info/', views.Tacher_create, name='info'),
    
    
    #working with viewss.py for api_view
    path('info-info/<int:primarykey>', viewss.Tacher_create, name='info'),
    path('info-info/', viewss.Tacher_create, name='info'),
    
    #working with viewsss.py for API using class-based views APIViews
    path('info-info/<int:primarykey>', viewsss.Tacher_create.as_view(), name='info'),
    path('info-info/', viewsss.Tacher_create.as_view(), name='info'),

]
