from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView, LogoutView 


urlpatterns = [
    path('api/adminprofile/', views.AdminProfileList.as_view(),name='adminprofiles'),
    path('api/neighborhood/', views.NeighList.as_view(),name='neighborhood'),
    path('api/occupantlist/', views.OccupantList.as_view(),name='occupant'),
    path('api/business/', views.BusinessList.as_view(),name='business'),


    
]