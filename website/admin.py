from django.contrib import admin
from .models import CustomUser,Batch,Internships,Extracurriculur,Mooc,Workshops,College,Department
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Batch)
admin.site.register(Internships)
admin.site.register(Extracurriculur)
admin.site.register(Mooc)
admin.site.register(Workshops)
admin.site.register(Department)
admin.site.register(College)