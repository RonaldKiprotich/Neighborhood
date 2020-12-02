from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProfile
        fields = ('user', 'profile_picture', 'bio')

class NeighSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeighbourHood
        fields = ('name', 'location', 'admin','hoodLogo','definition','occupants','emergencyNo')

class OccupantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupant
        fields = ('user', 'name', 'profile_pic','neighbourhood')

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('name', 'definition','email','neighbourhood','location')

