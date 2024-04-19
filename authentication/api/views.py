from rest_framework import generics
from django.contrib.auth import get_user_model
from authentication.api.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()  # Allow any to register
