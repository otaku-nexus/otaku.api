from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model
from authentication.api.serializers import ProfileSerializer
from rest_framework import mixins


class CreateUserView(generics.CreateAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = ()  # Allow any to register


class ProfileViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = ()  # Allow any to view, update, or delete
    lookup_field = "username"
    lookup_url_kwarg = "username"
