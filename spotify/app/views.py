from django.shortcuts import render
from .models import Artist, Song
# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse
from app.forms import ArtistForm , SongForm , CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import request,Http404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required



def index(request):
    songs= Song.objects.all()
    # songs = sorted(song_unsorted, key= lambda x: x.artist_avg, reverse=True)
    context = {'songs': songs}

    return render(request, 'app/index.html', context)


def rating(request, song_id, rate):
    if request.user.is_authenticated:
       song = Song.objects.get(pk=song_id)
       song.rating  = int(rate)
       song.save()
       return JsonResponse({}, status=200)
    else:
        return JsonResponse({},status=400)


@login_required(login_url='/login/')
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
            
            k = artist_form.save()
            id = k.id
            name = k.name
        return JsonResponse({'id':id, 'name':name}, status = 200)    

    return JsonResponse({}, status=400)

def loginUser(request):
    """ login form for user login """
    try:
        page = 'login'
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
                
        return render(request, 'app/login_register.html', {'page': page})     
    except Exception as e:
        print(e)
        raise Http404('Sorry some error occured')


def logoutUser(request):
    """ logout user """
    try:
        logout(request)
        return redirect('index')

    except Exception as e:
        
        raise Http404('Sorry some error occured')    

def registerUser(request):
    """ register form for new user """
    try:
        page = 'register'
        form = CustomUserCreationForm()

        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()

                if user is not None:
                    login(request, user)
                    return redirect('index')

        context = {'form': form, 'page': page}
        return render(request, 'app/login_register.html', context)    

    except Exception as e:
        
        raise Http404('Sorry some error occured')            