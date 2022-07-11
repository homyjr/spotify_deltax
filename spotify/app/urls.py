from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('rating/<int:song_id>/<str:rate>/',views.rating ,name="rating"),
    path('createsong/', views.add_song, name = "createsong")
]