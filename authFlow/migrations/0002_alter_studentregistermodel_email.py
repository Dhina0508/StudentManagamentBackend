# Generated by Django 5.0.2 on 2024-02-24 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authFlow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregistermodel',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
