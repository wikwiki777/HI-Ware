from django.urls import re_path, include
from accounts import views, urls_password_reset


urlpatterns = [
    re_path(r'^login$', views.login, name="login"),
    re_path(r'^register$', views.registration, name="register"),
    re_path(r'^profile$', views.profile, name="profile"),
    re_path(r'^logout$', views.logout, name="logout"),
    re_path(r'^password-reset/', include(urls_password_reset)),
]
