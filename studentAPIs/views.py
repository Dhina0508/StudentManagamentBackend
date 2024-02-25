from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from . import models
from . import serializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]


    def get(self,request,id=None):
        try:
            if id:
                student=models.StudentInfo.objects.get(id=id)
                serializer=serializers.StudentSerializer(student)
                return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"status":"error","message":"Student Not Found"},status=status.HTTP_404_NOT_FOUND)
        
        students=models.StudentInfo.objects.all()
        serializer=serializers.StudentSerializer(students,many=True)
        total=len(serializer.data)
        page = request.GET.get('page')
        count = request.GET.get('count')
        if page and count:
            data = serializer.data
            page = int(page)
            count = int(count)
            start = (page - 1)*count
            end = page*count
            end = end if end <= len(data) else len(data)
            
            return Response({"status":"success","page":page,"count":count,"total_data":total,
                            "data":data[start:end]},status=status.HTTP_200_OK)
        
        return Response({"status":"success",
                            "data":serializer.data},status=status.HTTP_200_OK)
    


    def post(self,request):
        serializer=serializers.StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","message":"Student Data Added Successfully"},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,id=None):
        try:
            student=models.StudentInfo.objects.get(id=id)
            serializer=serializers.StudentSerializer(student,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
            else:
                return Response({"status":"error","data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"status":"error","message":"Student Not Found"},status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,id=None):
        try:
            student=models.StudentInfo.objects.filter(id=id)
            student.delete()
            return Response({"status":"success","message":"Student Info Deleted Successfully"})
        except ObjectDoesNotExist:
            return Response({"status":"error","message":"Student Not Found"},status=status.HTTP_404_NOT_FOUND)
        

