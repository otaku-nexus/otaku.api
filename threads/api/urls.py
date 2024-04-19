from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ThreadViewSet, PostViewSet, LikeViewSet

router = DefaultRouter()
router.register(r'threads', ThreadViewSet)
router.register(r'posts', PostViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
