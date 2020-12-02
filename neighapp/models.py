
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from . models import *

# Create your models here.
class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image')
    bio = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username} AdminProfile'

    class Meta:
        db_table = 'adminprof'

class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey("AdminProfile", on_delete=models.CASCADE, related_name='neighborhood')
    hoodLogo = CloudinaryField('image')
    definition = models.TextField()
    occupants = models.IntegerField(null=True, blank=True)
    emergencyNo = models.IntegerField(null=True, blank=True)


    class Meta:
        db_table = 'neighborhood'
    

    def __str__(self):
        return f'{self.name} neighborhood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)


# Create your models here.
class Occupant(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    profile_pic = CloudinaryField('image')
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE, related_name='occupant')

class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='business')
    location = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()

