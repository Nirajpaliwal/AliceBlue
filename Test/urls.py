from django.contrib import admin
from django.urls import path, include
from TestAPI import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TestAPI.urls'))
]
