from django.shortcuts import render
from .models import Teacher
from .Serializers import TeacherSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

# Create your views here.
#QuerySet

def Teachers_Info(request):
    
    #Complex Data
    Teacher_data = Teacher.objects.all()
    
    #python Dictionary
    serializer_data = TeacherSerializers(Teacher_data, many = True)
    
    #render json
    json_data = JSONRenderer().render(serializer_data.data)
    
    #Json send to User
    return HttpResponse(json_data, content_type = 'application/json')

#get data for specific serial "http://127.0.0.1:8000/arena/details/primarykey"
def Teachers_(request, primarykey):
    
    #Complex Data
    Teacher_data = Teacher.objects.get(id = primarykey)
    serializer_data = TeacherSerializers(Teacher_data)
    json_data = JSONRenderer().render(serializer_data.data)
    
    return HttpResponse(json_data, content_type = 'application/json')

@csrf_exempt
def Tacher_create(request):
    if request.method == 'POST':
        json_data = request.body
        
        #Json to Stream convert
        stream = io.BytesIO(json_data)
        
        #Stream to Python convert
        python_data = JSONParser().parse(stream)
        
        #python to Complex Data
        serializer = TeacherSerializers(data=python_data)
        if serializer.is_valid():
            serializer.save()
            rs = {'msg': 'Successfully inserted'}
            json_dataa = JSONRenderer().render(rs)
            return HttpResponse(json_dataa, content_type = 'application/json')
        
        json_datas = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_datas, content_type = 'application/json')