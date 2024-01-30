from rest_framework import serializers
from .models import Teacher

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['techer_name', 
                  'course_name', 
                  'course_duration']



#if we use ModelSerializer instead of Serializer dont need to create manual method like 'Create', 'Update'


#Rename 'TeacherSerializers__' to 'TeacherSerializers' to persorm manual operation and comment out upper class.
class TeacherSerializers__(serializers.Serializer):
    
    techer_name = serializers.CharField(max_length = 30)
    course_name = serializers.CharField(max_length = 30)
    course_duration = serializers.IntegerField()
    
    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)
    
    def update(self, instance, validate_data):
        instance.techer_name = validate_data.get('techer_name', instance.techer_name)
        instance.course_name = validate_data.get('course_name', instance.course_name)
        instance.course_duration = validate_data.get('course_duration', instance.course_duration)
        
        instance.save()
        return instance