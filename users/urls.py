from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import (create_user_view, list_a_specific_user_view,
                    list_user_view, login_view)

urlpatterns = [
    path("users/register/", create_user_view.CreateUserView.as_view()),
    # path("users/login/", views.CustomLogin.as_view()),
    # path("users/login/", login_view.CustomLogin.as_view()),
    path("users/login/", obtain_auth_token),
    path("users/", list_user_view.ListUserView.as_view()),
    path("users/<int:user_id>/", list_a_specific_user_view.ListASpecificUser.as_view()),
]
