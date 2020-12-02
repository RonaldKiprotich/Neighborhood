from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *

# Create your views here.

class AdminProfileList(APIView):
    def get(self, request, format=None):
        all_merch = AdminProfile.objects.all()
        serializers = ProfileSerializer(all_merch, many=True)
        return Response(serializers.data)


