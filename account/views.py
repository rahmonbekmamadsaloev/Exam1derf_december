from django.shortcuts import render
from .models import CustomUser
from .serializer import RegisterSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login , logout

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class RegisterApi(APIView):

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=RegisterSerializer,
        responses={201: openapi.Response(description="User registered successfully"), 400: "Validation error"}
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'User registered successfully'},
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LoginApi(APIView):

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={200: openapi.Response(description="Login successful"),401: "Invalid credentials",400: "Validation error"}
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = authenticate(
                request=request,
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )

            if user:
                login(request, user)
                return Response(
                    {'message': 'Login successful'},
                    status=status.HTTP_200_OK
                )

            return Response(
                {'error': 'Invalid username or password'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    

class LogoutApi(APIView):

    @swagger_auto_schema(
        operation_description="Logout current user",
        responses={200: openapi.Response(description="Logout successful"),401: "Unauthorized"})
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'},status=status.HTTP_200_OK)
