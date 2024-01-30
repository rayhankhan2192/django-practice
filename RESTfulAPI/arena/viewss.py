from django.shortcuts import render
from .models import Teacher
from .Serializers import TeacherSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def Tacher_create(request, primarykey = None):
    if request.method == 'GET':
        id = primarykey
        if id is not None:
            #Complex Data
            data = Teacher.objects.get(id = id)
            #python dictionaries
            serializer = TeacherSerializers(data)
            return Response(serializer.data)
        data = Teacher.objects.all()
        serializer = TeacherSerializers(data, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = TeacherSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully inserted'})
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        id = primarykey
        id_data = Teacher.objects.get(id = id)
        serializer = TeacherSerializers(id_data, data=request.data, partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully all data Updated'})
        return Response(serializer.errors)
    
    if request.method == 'PATCH':
        id = primarykey
        id_data = Teacher.objects.get(id = id)
        serializer = TeacherSerializers(id_data, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully Partially Updated'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = primarykey
        id_data = Teacher.objects.get(id = id)
        id_data.delete()
        return Response({'msg': 'Successfully Deleted'})