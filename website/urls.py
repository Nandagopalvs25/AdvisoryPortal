from django.urls import path, include
from .views import index, dashboard, certificates, mooc, internship, extrac, workshops, student_uploads_view, advisor_studentsList, delete, advisor_approval_view, advisor_approve_upload_view,advisor_student_profile_view


urlpatterns = [

    path("", index, name='homepage'),
    path("dashboard/", dashboard, name='dashboard'),
    path("studentslist/", advisor_studentsList, name='advisor_studentslist'),
    path("studentProfile/<int:id>/", advisor_student_profile_view, name='advisor_student_profile_url'),
    path("certificates/", certificates, name='certificate'),
    path("uploads/", student_uploads_view, name='student_uploads_view'),
    path("approvals/", advisor_approval_view, name='advisor_approval_view'),
    path("approve/<int:id>", advisor_approve_upload_view,name='check_approval_view'),
    path("uploads/delete/<str:model_name>/<int:id>/",delete, name='delete_object'),
    path("certificates/mooc/", mooc, name='mooc'),
    path("certificates/internships/", internship, name='internship'),
    path("certificates/extrac/", extrac, name='extrac'),
    path("certificates/workshops/", workshops, name='workshops'),
    path("auth/", include('allauth.urls')),
]
