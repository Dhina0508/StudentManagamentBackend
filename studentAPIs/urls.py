from django.urls import path
from .views import StudentView

urlpatterns=[
    path('student/',StudentView.as_view()),
    path('student/<int:id>',StudentView.as_view()),
    # path('uploadFile/', upload_file, name='upload')
    #  path('upload-image/', upload_image, name='upload_image'),
]

