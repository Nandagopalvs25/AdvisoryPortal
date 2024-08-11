from django.urls import path,include
from .views import index,dashboard,certificates,mooc,internship,extrac,workshops,uploads_view,studentsList,deleteMooc,deleteExtrac,deleteWorkshops,deleteIntern


urlpatterns = [
  
    path("",index,name='homepage'),
    path("dashboard/",dashboard,name='dashboard'),
    path("studentslist/",studentsList,name='studentslist'),
    path("certificates/",certificates,name='certificate'),
    path("uploads/",uploads_view,name='uploads_view'),
    path("uploads/mooc/delete/<int:id>",deleteMooc,name='del_mooc'),
    path("uploads/intern/delete/<int:id>",deleteExtrac,name='del_internship'),
    path("uploads/extrac/delete/<int:id>",deleteIntern,name='del_extracurricular'),
    path("uploads/workshop/delete/<int:id>",deleteWorkshops,name='del_workshop'),
    path("certificates/mooc/",mooc,name='mooc'),
    path("certificates/internships/",internship,name='internship'),
    path("certificates/extrac/",extrac,name='extrac'),
    path("certificates/workshops/",workshops,name='workshops'),
    path("auth/",include('allauth.urls')),
]
