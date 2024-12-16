from django.urls import path,include
from .views import index,dashboard,certificates,mooc,internship,extrac,workshops,student_uploads_view,studentsList,delete, advisor_approval_view


urlpatterns = [
  
    path("",index,name='homepage'),
    path("dashboard/",dashboard,name='dashboard'),
    path("studentslist/",studentsList,name='studentslist'),
    path("certificates/",certificates,name='certificate'),
    path("uploads/",student_uploads_view,name='uploads_view'),
    path("approvals/",advisor_approval_view,name='approval_view'),

    path("uploads/delete/<str:model_name>/<int:id>/", delete, name='delete_object'),
    path("certificates/mooc/",mooc,name='mooc'),
    path("certificates/internships/",internship,name='internship'),
    path("certificates/extrac/",extrac,name='extrac'),
    path("certificates/workshops/",workshops,name='workshops'),
    path("auth/",include('allauth.urls')),
]
