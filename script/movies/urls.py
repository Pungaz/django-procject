from django.urls import path, re_path
from . import views, charts

app_name = 'movies'
urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('movies/', views.movies, name='movies'),
    path('movie/edit/<int:id>', views.edit, name='edit'),
    path('movie/new/', views.new, name='new'),
    path('movies/unRent/<int:id>', views.unRent, name='unRent'),
    path('movies/remove/<int:id>', views.remove, name='remove'),
    path('register/', views.register, name='register'),
    path('rented/', views.rented, name='rented'),
    path('chart/', charts.chart, name='chart')
]
