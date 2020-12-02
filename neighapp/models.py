from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Occupant(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    profile_pic = CloudinaryField('image')
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE, related_name='occupant')

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

