import json
from product.models import Product
from django.forms.models import model_to_dict

from django.http import JsonResponse, HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # Manual Operation
        
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        
        # Serializer
        # model instance(model_data)
        # turn into py dict
        # return JSON to client
        
        data = model_to_dict(model_data)
        
        #we can customisez filed view to client
        #data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    
    return JsonResponse(data)

from product.serializer import Product_Serializer

"""
Django APi View
"""
@api_view(['GET'])
def api_home_get(request, *args, **kwargs):
    #model_data = Product.objects.all().order_by("?").first()
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        #data = model_to_dict(instance)
        data = Product_Serializer(instance).data
        return Response(data)
    
@api_view(['POST'])
def api_home_post(request, *args, **kwargs):
    
    #instance_data = request.data
    serializer = Product_Serializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        #instance_data = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({'error': "Invalid Data Field"}, status=400)