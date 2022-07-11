from django.shortcuts import render
from .models import Artist, Song
# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse




def index(request):
    songs= Song.objects.all()
    # songs = sorted(song_unsorted, key= lambda x: x.artist_avg, reverse=True)
    context = {'songs': songs}

    return render(request, 'app/index.html', context)


def rating(request, song_id, rate):
       
       song = Song.objects.get(pk=song_id)
       song.rating  = int(rate)
       song.save()
       return JsonResponse({}, status=200)