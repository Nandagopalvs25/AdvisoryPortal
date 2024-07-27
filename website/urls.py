from django.urls import path,include
from .views import index,dashboard,certificates,mooc,internship,extrac,workshops,uploads_view,studentsList


urlpatterns = [
  
    path("",index,name='homepage'),
    path("dashboard/",dashboard,name='dashboard'),
    path("studentslist/",studentsList,name='studentslist'),
    path("certificates/",certificates,name='certificate'),
    path("uploads/",uploads_view,name='uploads_view'),
    path("certificates/mooc/",mooc,name='mooc'),
    path("certificates/internships/",internship,name='internship'),
    path("certificates/extrac/",extrac,name='extrac'),
    path("certificates/workshops/",workshops,name='workshops'),
    path("auth/",include('allauth.urls')),
]
