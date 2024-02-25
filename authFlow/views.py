from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from .serializers import StudentSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate


class RegisterStudent(APIView):
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            try:                
                serializer.save()
                return Response({
                    'status': 200,
                    'payload': serializer.data,
                    'message': "Your Registered Successfully"
                })
            except IntegrityError:
                return Response({'status': 500, 'errors': 'Email already exists', 'message': 'Student Already Exists'})
        return Response({'Status': 403, 'errors': serializer.errors, 'message': 'Something Went Wrong'})
    


class LoginStudent(APIView):
    def post(self, request):
        email = request.data['username']
        password = request.data['password']
        print(request.data)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({'status': 200, 'payload': request.data,
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token),'message':"Logged In Successfully"})
    
        return Response({'Status': 400, 'errors': "error", 'message': 'Invalid Credentails'})



class RefreshAccessToken(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            return Response({'status': 400, 'message': 'Refresh token is required'})

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            return Response({'status': 200, 'access_token': access_token,'refresh_token':str(refresh), 'message': 'Access token refreshed successfully'})
        except Exception as e:
            return Response({'status': 400, 'message': str(e)})