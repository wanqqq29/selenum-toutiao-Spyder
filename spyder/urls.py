import spyder.views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('go/',spyder.views.go),
]
