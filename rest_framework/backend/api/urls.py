from django.urls import path, include
from .import views

urlpatterns = [
    path('api/', views.api_home),
    path('get/', views.api_home_get),
    path('post/', views.api_home_post),
    
    
    #path('product/', include('product.urls'))
]
