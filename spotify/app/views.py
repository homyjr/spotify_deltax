from django.shortcuts import render
from .models import Artist, Song
# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse
from app.forms import ArtistForm , SongForm



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


def add_song(request):

    if request.method == "POST":
        form = SongForm(request.POST ,request.FILES, initial ={'rating':'0'})
        if form.is_valid():
            form.save()
            return JsonResponse({"s":"success"}, status=200)
    else:      
        form = SongForm() 
    context = {
        'form': form
    }
    return render(request, 'app/song.html', context)


def add_artist(request):
    if request.method == "POST":
        artist_form = ArtistForm(request.POST)
        if artist_form.is_valid():
            print("yes")
            k = artist_form.save()
            id = k.id
            name = k.name
        return JsonResponse({'id':id, 'name':name}, status = 200)    

    return JsonResponse({}, status=400)

