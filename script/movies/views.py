import time

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from .forms import MovieForm
from .models import Movie


def landing_page(req):
    if not req.user.is_authenticated:
        return render(req, 'landing_page.html', {'page_title': 'Ovde cemo se login-ovati'})
    else:
        return redirect('movies:movies')


@login_required
def movies(req):
    movies_list = Movie.objects.order_by('title')
    return render(req, 'movies.html', {'movies': movies_list})


@permission_required('movies.change_movie')
def edit(req, id):
    if req.method == 'POST':
        form = MovieForm(req.POST)

        if form.is_valid():
            movie_object = Movie.objects.get(pk=id)
            movie_object.title = form.cleaned_data['title']
            movie_object.description = form.cleaned_data['description']
            movie_object.rented = form.cleaned_data['rented']
            movie_object.save()
            return redirect('movies:movies')
        else:
            return render(req, 'edit.html', {'form': form, 'id': id})
    else:
        movie_object = get_object_or_404(Movie, pk=id)
        form = MovieForm(instance=movie_object)
        return render(req, 'edit.html', {'form': form, 'id': id})


@permission_required('movies.add_movie')
def new(req):
    if req.method == 'POST':
        form = MovieForm(req.POST)
        vreme = int(time.time() * 1000)
        if form.is_valid():
            movie_object = Movie(title=form.cleaned_data['title'], description=form.cleaned_data['description'],
                                 rented=False, rented_count=0, created_at=vreme,
                                 updated_at=vreme, release_date=form.cleaned_data['release_date'],
                                 rating=form.cleaned_data['rating'])
            movie_object.save()
            return redirect('movies:movies')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = MovieForm()
        return render(req, 'new.html', {'form': form})


@login_required
def unRent(req, id):
    if req.method == 'POST':
        movie_object = Movie.objects.get(pk=id)
        movie_object.user = None
        movie_object.rented = False
        movie_object.save()
    return redirect('movies:rented')


@permission_required('movies.delete_movie')
def remove(req, id):
    if req.method == 'POST':
        Movie.objects.filter(pk=id).delete()
    return redirect('movies:movies')


def register(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:movies')
    else:
        form = UserCreationForm()
    return render(req, 'register.html', {'form': form})


@login_required
def rented(req):
    movies_list = Movie.objects.filter(user=req.user.id)
    return render(req, 'rented_movies.html', {'movies': movies_list})
