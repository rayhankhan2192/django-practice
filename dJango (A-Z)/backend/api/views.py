from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict


from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API view
    """
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        #rest framework
        data = model_to_dict(model_data, fields=['id','title', 'content', 'price'])
    return Response(data)
        
        
        
        
        #..................................................
        #request -> HttpRequest -< Django
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['priice'] = model_data.price 
        
        # model instant (model_data)
        # turn into python dict
        # return json to client 
    #     data = model_to_dict(model_data, fields=['id','title', 'content', 'price'])  
    # return JsonResponse(data)
        
    #     data = model_to_dict(model_data, fields=['id','title', 'content', 'price'])  
    #     data = dict(data)
    #     json_data = json.dumps(data)
    # return HttpResponse(json_data, headers={'content-type': "application/json"})