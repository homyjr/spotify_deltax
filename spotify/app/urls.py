from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('rating/<int:song_id>/<str:rate>/',views.rating ,name="rating"),
    path('createsong/', views.add_song, name = "createsong"),
    path('createartist/', views.add_artist, name="createartist" ),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('allartists/', views.allartists, name="allartists"),
    path('allsongs/', views.allsongs, name="allsongs"),
]