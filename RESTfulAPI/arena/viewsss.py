from django.shortcuts import render
from .models import Teacher
from .Serializers import TeacherSerializers
from rest_framework.views import APIView
from rest_framework.response import Response


class Tacher_create(APIView):
    def get(self, request, primarykey = None, format = None):
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
    
    def post(self, request, format = None):
        serializer = TeacherSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully inserted'})
        return Response(serializer.errors)
    
    def put(self, request, primarykey, format = None):
        id = primarykey
        id_data = Teacher.objects.get(id = id)
        serializer = TeacherSerializers(id_data, data=request.data, partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully all data Updated'})
        return Response(serializer.errors)
    
    def patch(self, request, primarykey, format = None):
        id = primarykey
        id_data = Teacher.objects.get(id = id)
        serializer = TeacherSerializers(id_data, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully Partially Updated'})
        return Response(serializer.errors)
    
    def delete(self, request, primarykey, format = None):
        id = primarykey
        id_data = Teacher.objects.get(id = id)
        id_data.delete()
        return Response({'msg': 'Successfully Deleted'})