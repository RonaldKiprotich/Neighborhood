from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProfile
        fields = ('user', 'profile_pic', 'bio')

class NeighSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeighbourHood
        fields = ('name', 'location', 'admin','hoodLogo','definition','occupants','emergencyNo')