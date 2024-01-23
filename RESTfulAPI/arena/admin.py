from django.contrib import admin
from .models import Teacher

# Register your models here.
@admin.register(Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ['id', 'techer_name', 
                    'course_name', 
                    'course_duration']
    
#also we can write

# class Teacher(admin.ModelAdmin):
#     list_display = ['id', 'techer_name', 
#                     'course_name', 
#                     'course_duration']
# admin.site.register(Teacher)