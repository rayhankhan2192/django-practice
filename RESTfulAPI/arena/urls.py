from django.urls import path, include
from .import views, viewss, viewsss, views_mixing, views_modelviewset

from rest_framework.routers import DefaultRouter

#router object
router = DefaultRouter()
#register router
router.register('info-modelView', views_modelviewset.Teacher_create, 
                basename='info')

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
    
    #working with views_mixing.py for class based view in mixing
    #http://127.0.0.1:8000/arena/info-withMixing/
    path('info-withMixing/<int:primarykey>', views_mixing.TeacherList.as_view(), name='info'),
    path('info-withMixing/', views_mixing.TeacherList.as_view(), name='info'),
    
    # http://127.0.0.1:8000/arena/info-withMixing-view/<int:pk>/
    path('info-withMixing-view/<int:pk>/', views_mixing.TacacherDetails.as_view(), name='info'),
    
    #http://127.0.0.1:8000/info-modelView/
    path('', include(router.urls))

]
