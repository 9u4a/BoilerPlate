from django.urls import path, include
from Views.UserView import UserView
from Views.LoginView import LoginView

urlpatterns = [
    path('user/', UserView.as_view()),
    path('login/', LoginView.as_view()),
]
