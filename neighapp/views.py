
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .forms import RegistrationForm
from rest_framework import viewsets,status,generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class AdminProfileList(APIView):
    def get(self, request, format=None):
        all_merch = AdminProfile.objects.all()
        serializers = ProfileSerializer(all_merch, many=True)
        return Response(serializers.data)

class NeighList(APIView):
    def get(self, request, format=None):
        all_merch = NeighbourHood.objects.all()
        serializers = NeighSerializer(all_merch, many=True)
        return Response(serializers.data)

class OccupantList(APIView):
    def get(self, request, format=None):
        all_merch = Occupant.objects.all()
        serializers = OccupantSerializer(all_merch, many=True)
        return Response(serializers.data)

class BusinessList(APIView):
    def get(self, request, format=None):
        all_merch = Business.objects.all()
        serializers = BusinessSerializer(all_merch, many=True)
        return Response(serializers.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSignupSerializer
    queryset = User.objects.all()

class LogoutAPIView(generics.CreateAPIView):
    serializer_class=LogoutSerializer
    permission_classes=(IsAuthenticated,)
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        token=request.data.get('refresh_token')
        error_message={
            "error":"Token is invalid or expired"
        }
        success_message={
            "success":"Logout successfully"
        }        
        try:
            token=RefreshToken(token)
            token.blacklist()
        except TokenError as error:
            return Response(error_message,status=status.HTTP_400_BAD_REQUEST)
        return Response(success_message,status=status.HTTP_200_OK)


class PostList(APIView):

    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)   