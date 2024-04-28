from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model
from authentication.api.serializers import ProfileSerializer

class CreateUserView(generics.CreateAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = ()  # Allow any to register

class ProfileViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = ()  # Allow any to view, update, or delete
    lookup_field = "username"
    lookup_url_kwarg = "username"
