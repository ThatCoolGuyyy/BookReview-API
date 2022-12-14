from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.views import registration_view


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('registration/', registration_view.as_view(), name='registration')
]
