from django.forms import ModelForm
from .models import Movie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'rented', 'description', 'release_date', 'rating')
