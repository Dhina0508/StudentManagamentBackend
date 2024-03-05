from django.db import models

class StudentInfo(models.Model):
    fullName=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    mobile=models.BigIntegerField()
    address=models.TextField(max_length=100)
    graduated=models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
