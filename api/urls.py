from django.urls import include,path
from .views import UserView


urlpatterns = [
   
    path('auth/', include('dj_rest_auth.urls')),
    path('users/',UserView.as_view() ),
    path('auth/registration/', include('dj_rest_auth.registration.urls'))
]