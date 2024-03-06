from django.urls import path
from .views import StudentView,ExternalAPICall

urlpatterns=[
    path('student/',StudentView.as_view()),
    path('student/<int:id>',StudentView.as_view()),
    path('external-data',ExternalAPICall.as_view())

]

