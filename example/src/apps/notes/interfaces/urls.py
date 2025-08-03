"""
URL configuration for the notes app.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from apps.my_app.interfaces import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from apps.other_app.interfaces.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.notes.interfaces.views import NoteViewSet

router = DefaultRouter()
router.register("", NoteViewSet, basename="note")

urlpatterns = [
    path("", include(router.urls)),
]
