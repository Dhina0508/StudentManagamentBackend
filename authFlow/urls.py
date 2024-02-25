from django.urls import path
from .views import RegisterStudent,LoginStudent,RefreshAccessToken
# from .views import register_user
urlpatterns=[
    path('register/',RegisterStudent.as_view()),
    path('login/',LoginStudent.as_view()),
    path('refresh_token/',RefreshAccessToken.as_view()),



]