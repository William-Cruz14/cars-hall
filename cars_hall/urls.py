from django.contrib import admin
from django.urls import path
from cars_hall.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]