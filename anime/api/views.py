from rest_framework import generics, viewsets
from ..models import Anime
from .serializers import AnimeSerializer
from rest_framework import mixins

class AnimeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = ()
    lookup_field = 'mal_id'
    lookup_url_kwarg = 'mal_id'