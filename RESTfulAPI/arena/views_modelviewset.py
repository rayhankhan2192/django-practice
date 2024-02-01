from .models import Teacher
from .Serializers import TeacherSerializers
from rest_framework import viewsets


class Teacher_create(viewsets.ModelViewSet):
    queryset  = Teacher.objects.all()
    serializer_class = TeacherSerializers