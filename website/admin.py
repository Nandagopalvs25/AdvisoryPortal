from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  
from .models import CustomUser,Batch,Internships,Extracurriculur,Mooc,Workshops,College,Department,Student,Advisor
# Register your models here.



class StudentInline(admin.TabularInline):
    model = Student
    

class AdvisorInline(admin.TabularInline):
    model = Advisor

class CustomUserAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,AdvisorInline,
    ]

admin.site.register(Batch)
admin.site.register(Internships)
admin.site.register(Extracurriculur)
admin.site.register(Mooc)
admin.site.register(Workshops)
admin.site.register(Department)
admin.site.register(College)
admin.site.register(CustomUser, CustomUserAdmin)


