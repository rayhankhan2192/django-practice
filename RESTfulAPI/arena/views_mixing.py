"""
Using mixins

"""

from .models import Teacher
from .Serializers import TeacherSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import CreateModelMixin

class TeacherList(GenericAPIView, 
                  ListModelMixin,
                  CreateModelMixin):
    queryset  = Teacher.objects.all()
    serializer_class = TeacherSerializers
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
from rest_framework import mixins
from rest_framework import generics

class TacacherDetails(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    
    queryset  = Teacher.objects.all()
    serializer_class = TeacherSerializers
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
   
# Using generic class-based views

class TeacherListGeneric(generics.ListCreateAPIView):
    queryset  = Teacher.objects.all()
    serializer_class = TeacherSerializers

class TacacherDetailsGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset  = Teacher.objects.all()
    serializer_class = TeacherSerializers       
    