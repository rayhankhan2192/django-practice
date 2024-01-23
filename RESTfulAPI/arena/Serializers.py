from rest_framework import serializers
from .models import Teacher


class TeacherSerializers(serializers.Serializer):
    
    techer_name = serializers.CharField(max_length = 30)
    course_name = serializers.CharField(max_length = 30)
    course_duration = serializers.IntegerField()
    
    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)