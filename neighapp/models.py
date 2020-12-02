from django.db import models


# Create your models here.
class Occupant(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField()
    profile_pic = CloudinaryField()
    neighbourhood = models.ForeignKey(Neighbourhood)
class Business(models.Model):
    name = models.CharField()
    definition = models.CharField()
    email = models.EmailField()
    neighbourhood = models.ForeignKey(Neighbourhood)
    location = LocationField()

