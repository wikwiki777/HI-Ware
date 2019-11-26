from django.urls import re_path
from accounts import views


urlpatterns = [
    re_path(r'^login$', views.login, name="login"),
    re_path(r'^register$', views.registration, name="register"),
]
