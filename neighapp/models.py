from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Business(models.Model):
    name = models.CharField()
    definition = models.CharField()
    email = models.EmailField()
    neighbourhood = models.ForeignKey(Neighbourhood)
    location = LocationField()


class Occupant(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField()
    profile_pic = CloudinaryField()
    neighbourhood = models.ForeignKey(Neighbourhood)
