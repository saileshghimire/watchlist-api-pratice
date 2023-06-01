from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from user_app.api.views import register_view, logout_view


urlpatterns = [
    path('login/', obtain_auth_token, name="login"),
    path('register/', register_view.as_view(), name="register"),
    path('logout/', logout_view.as_view(), name="logout"),

]
