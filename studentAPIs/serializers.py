from rest_framework import serializers
from .models import StudentInfo


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = '__all__'

    # def create(self, validated_data):
    #     image_file = validated_data.pop('image')
    #     student = StudentInfo.objects.create(**validated_data)
    #     student.image.save(image_file.name, image_file)
    #     return student
