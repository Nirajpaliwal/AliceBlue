from django.contrib import admin
from TestAPI.models import Registration, Profile
# Register your models here.

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'password']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['gender', 'dob', 'address', 'pincode', 'state', 'nationality', 'registration']