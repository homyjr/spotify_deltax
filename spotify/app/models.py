from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models import Sum, Avg
# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=255)
    dateofbirth = models.DateField(blank = True, null=True)
    bio = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name

    @property 
    def artist_avg(self):
        queryset = self.song_set.all().filter(rating__gt=0).aggregate(Avg('rating'))
        if(queryset['rating__avg'] == None):
            return 0
        else:
            return int(queryset['rating__avg'])
   


class Song(models.Model):
    artists = models.ManyToManyField(Artist)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    date = models.DateField(blank = True, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)], default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-rating']