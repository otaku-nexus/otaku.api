from django.db import models
from django.utils import timezone

# Create your models here.
class Anime(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.TextField()
    mal_id = models.IntegerField(unique=True)
    type = models.ForeignKey('AnimeType', on_delete=models.CASCADE)
    episode_count = models.IntegerField()
    image = models.ImageField(upload_to='anime_pictures', default='anime_pictures/default.jpg')
    airing = models.BooleanField(blank=True, null=True)
    aired_from = models.DateTimeField(blank=True, null=True)
    aired_to = models.DateTimeField(blank=True, null=True)
    age_rating = models.CharField(max_length=10, null=True)
    mal_score = models.FloatField(blank=True, null=True)
    mal_rank = models.IntegerField(blank=True, null=True)
    season = models.CharField(max_length=20, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    broadcasting_time = models.CharField(max_length=20, blank=True, null=True)
    studio = models.CharField(max_length=50, blank=True, null=True)
    
    
    def __str__(self):
        return self.title
    
class AnimeType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
        
    def __str__(self):
        return self.name

class Episodes(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.TextField()
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE)
    episode_number = models.IntegerField()
    duration = models.IntegerField()
    aired = models.DateTimeField()
    filler = models.BooleanField()
    recap = models.BooleanField()
    mal_url = models.URLField()
    
    def __str__(self):
        return self.title
    
    
class Rating(models.Model):
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE)
    user = models.ForeignKey('authentication.Profile', on_delete=models.CASCADE)
    rating = models.IntegerField()
    
    def __str__(self):
        return f'{self.user}\'s rating of {self.anime}'
    
class Favorite(models.Model):
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE)
    user = models.ForeignKey('authentication.Profile', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user}\'s favorite anime {self.anime}'
    
class Genres(models.Model):
    name = models.CharField(max_length=50)
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} of {self.anime}'
    
class CurrentlyWatching(models.Model):
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE)
    user = models.ForeignKey('authentication.Profile', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user} is currently watching {self.anime}'
    
class Completed(models.Model):
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE)
    user = models.ForeignKey('authentication.Profile', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user} has completed {self.anime}'