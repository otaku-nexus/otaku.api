from rest_framework import serializers
from ..models import Anime, AnimeType, Episodes, Rating, Favorite, Genres, CurrentlyWatching, Completed


class AnimeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeType
        fields = '__all__'

class AnimeSerializer(serializers.ModelSerializer):
    type = AnimeTypeSerializer()

    class Meta:
        model = Anime
        fields = '__all__'

class EpisodesSerializer(serializers.ModelSerializer):
    anime = AnimeSerializer()

    class Meta:
        model = Episodes
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class GenresSerializer(serializers.ModelSerializer):
    anime = AnimeSerializer()

    class Meta:
        model = Genres
        fields = '__all__'

class CurrentlyWatchingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentlyWatching
        fields = '__all__'

class CompletedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Completed
        fields = '__all__'