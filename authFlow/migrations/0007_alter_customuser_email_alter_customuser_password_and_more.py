# Generated by Django 5.0.2 on 2024-02-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authFlow', '0006_customuser_delete_studentloginmodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
