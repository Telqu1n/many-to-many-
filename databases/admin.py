from django.contrib import admin
from .models import student, teacher
# Register your models here.

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'address']
    
@admin.register(teacher)
class teacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'address']
    
