from django.urls import path
from .import views

#/api/product/
urlpatterns = [

    #GenericApiView
    # path('<int:pk>', views.Product_Detail_view),
    # path('create/', views.Product_create_view),
    
    #ListAPIView
    # path('create/', views.Product_create_List_view),
    # path('view/', views.Product_list_view),
    
    # path('create/', views.product_alt_view),
    # path('view/', views.product_alt_view),
    # path('view/<int:pk>', views.product_alt_view),
    
    path('view/<int:pk>/delete/', views.Product_destroy_view),
    path('view/<int:pk>/update/', views.Product_update_view),
]
