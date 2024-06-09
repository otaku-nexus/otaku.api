from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register(r'', AnimeViewSet, basename='anime')

urlpatterns = [
    path('', include(router.urls)),
    # Add more URL patterns for your API views here
]