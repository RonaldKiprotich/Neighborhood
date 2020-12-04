from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AdminProfile)
admin.site.register(NeighbourHood)
admin.site.register(Business)
admin.site.register(Occupant)
admin.site.register(Post)

