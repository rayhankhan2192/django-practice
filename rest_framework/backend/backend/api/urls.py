from django.urls import path, include
from .import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('api/', views.api_home),
    path('get/', views.api_home_get),
    path('post/', views.api_home_post),
    
    #path('product/', include('product.urls'))
]
