from rest_framework import generics

from .models import Product
from .serializer import Product_Serializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404
from django.shortcuts import get_object_or_404


from rest_framework import permissions
from rest_framework import authentication

from .permission import IsStaffEditionPermission


"""
generic RetriveApi
"""
class ProductDetailsAPIview(generics.RetrieveAPIView):
    queryset = Product.objects.all()    
    serializer_class = Product_Serializer
Product_Detail_view = ProductDetailsAPIview.as_view()

class ProductUpdateAPIview(generics.UpdateAPIView):
    queryset = Product.objects.all()    
    serializer_class = Product_Serializer
    lookup_field = 'pk'
    def perform_update(self, serializer):
       serializer.save()
Product_update_view = ProductUpdateAPIview.as_view()

class ProductDeleteAPIview(generics.DestroyAPIView):
    queryset = Product.objects.all()    
    serializer_class = Product_Serializer
    lookup_field = 'pk'
    def perform_destroy(self, instance):
       super().perform_destroy(instance)
Product_destroy_view = ProductDeleteAPIview.as_view()
    
    
class ProductCreateAPIview(generics.CreateAPIView):
    queryset = Product.objects.all()    
    serializer_class = Product_Serializer
    
    def perform_create(self, serializer):
        print(serializer.validated_data)
        serializer.save()
Product_create_view = ProductCreateAPIview.as_view()
   

"""
ListAPIView
"""

class ProductListAPIview(generics.ListAPIView):
    queryset = Product.objects.all()    
    serializer_class = Product_Serializer
    permission_classes = [permissions.IsAuthenticated]
    
Product_list_view = ProductListAPIview.as_view()


class ProductCreateListAPIview(generics.ListCreateAPIView):
    queryset = Product.objects.all()    
    serializer_class = Product_Serializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
    ]
    permission_classes = [permissions.IsAdminUser, IsStaffEditionPermission]
    
    def perform_create(self, serializer):
        print(serializer.validated_data)
        serializer.save()
Product_create_List_view = ProductCreateListAPIview.as_view()
   
   
   
@api_view(['GET', 'POST'])  
def product_alt_view(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            #detail view
            # queryset = Product.objects.filter(pk = pk)
            # if not queryset.exist():
            #     raise Http404
            obj = get_object_or_404(Product, pk = pk)
            data = Product_Serializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all()
        data = Product_Serializer(queryset, many = True).data
        return Response(data)
        
    if request.method == 'POST':
        #instance_data = request.data
        serializer = Product_Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response({'error': "Invalid Data Field"}, status=400)