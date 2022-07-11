from django.forms import ModelForm, widgets 
from app.models import Artist, Song

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
            {'class': 'form-select', 'multiple':'' ,'aria-label':'multiple select example'})


