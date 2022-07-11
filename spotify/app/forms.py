from django.forms import ModelForm, widgets 
from app.models import Artist, Song
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"


class SongForm(ModelForm):
    class Meta:
        model = Song
        exclude = ['rating']
        widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(SongForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter title...'})
        self.fields['artists'].widget.attrs.update(
            {'id':'artist-field-id','class': 'form-select', 'multiple':'' ,'aria-label':'multiple select example'})

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter username...'}),
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter password...'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Confirm password...'})        
