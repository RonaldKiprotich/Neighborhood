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
        fields = ('name', 'description','email','neighbourhood','location')

class UserSignupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

