from django.contrib import admin
from .models import CustomUser,Batches,Internships,Extracurriculur,Mooc,Workshops
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Batches)
admin.site.register(Internships)
admin.site.register(Extracurriculur)
admin.site.register(Mooc)
admin.site.register(Workshops)