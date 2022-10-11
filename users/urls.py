from xml.etree.ElementInclude import include
from django.urls import path

from . import views


urlpatterns = [
    path("users/register/", views.UserView.as_view()),
    path("users/login/", views.CustomLogin.as_view()),
]
