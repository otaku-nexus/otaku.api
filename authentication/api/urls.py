from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authentication.api import views
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register(r'users', views.ProfileViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', views.CreateUserView.as_view(), name='signup'),
]
