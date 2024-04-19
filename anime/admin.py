from django.contrib import admin
from .models import Anime, AnimeType, Episodes, Rating, Favorite, Genres, CurrentlyWatching
# Register your models here.
admin.site.register(Anime)
admin.site.register(AnimeType)
admin.site.register(Episodes)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(Genres)
admin.site.register(CurrentlyWatching)

