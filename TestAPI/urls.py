from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('registeruser/', views.registerUser, name='registeruser'),
    path('profile/', views.profile, name='profile'),
    path('registerprofile/', views.registerProfile, name='registerprofile'),
    path('login/', views.login, name='login'),
    path('authenticateuser/', views.authenticateuser, name='authenticateuser'),
    # path('getuserdetails/', views.getuserdetails, name='getuserdetails'),
    
]
