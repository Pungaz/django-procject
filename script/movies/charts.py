import pygal
from django.shortcuts import render

from .models import MovieUser, User, Movie


def chart(req):
    transactions = MovieUser.objects.all()
    users = User.objects.all()
    bar_chart1 = pygal.Pie()
    bar_chart1.title = "Koji user je sta rentirao"
    num_of_rents_per_user_id_dict = {}
    num_of_rents_per_user_dict = {}
    for transaction in transactions:
        if transaction.rented:
            if transaction.user_id not in num_of_rents_per_user_id_dict:
                num_of_rents_per_user_id_dict[transaction.user_id] = 1
            else:
                num_of_rents_per_user_id_dict[transaction.user_id] += 1

    for x in users:
        for temp in num_of_rents_per_user_id_dict:
            if x.id == temp:
                num_of_rents_per_user_dict[x.username] = num_of_rents_per_user_id_dict[temp]

    for key in num_of_rents_per_user_dict:
        bar_chart1.add(key, num_of_rents_per_user_dict[key])

    bar_chart1.render_to_file('/home/bogdan/PycharmProjects/project/script/movies/static/charts/chart1.svg')

    movies = Movie.objects.all()
    bar_chart2 = pygal.Pie()
    bar_chart2.title = "Ukupan broj rentiranih filmova po userima"
    num_of_rents_per_movie_id_dict = {}
    num_of_rents_per_movie_dict = {}
    for transaction in transactions:
        if transaction.rented:
            if transaction.movie_id not in num_of_rents_per_movie_id_dict:
                num_of_rents_per_movie_id_dict[transaction.movie_id] = 1
            else:
                num_of_rents_per_movie_id_dict[transaction.movie_id] += 1

    for x in movies:
        for temp in num_of_rents_per_movie_id_dict:
            if x.id == temp:
                num_of_rents_per_movie_dict[x.title] = num_of_rents_per_movie_id_dict[temp]

    for key in num_of_rents_per_movie_dict:
        bar_chart2.add(key, num_of_rents_per_movie_dict[key])

    bar_chart2.render_to_file('/home/bogdan/PycharmProjects/project/script/movies/static/charts/chart2.svg')

    all_time_rented_movies_id = {}
    all_time_rented_movies = {}
    bar_chart3 = pygal.Bar()
    bar_chart3.title = "Broj rentiranja svakog filma od strane odabranog usera"
    id_user = req.GET.get('iduser')

    if id_user:
        for transaction in transactions:
            if transaction.rented:
                if transaction.user_id == int(id_user):
                    if transaction.movie_id not in all_time_rented_movies_id:
                        all_time_rented_movies_id[transaction.movie_id] = 1
                    else:
                        all_time_rented_movies_id[transaction.movie_id] += 1

        for x in movies:
            for temp in all_time_rented_movies_id:
                if x.id == temp:
                    all_time_rented_movies[x.title] = all_time_rented_movies_id[temp]

        for key in all_time_rented_movies:
            bar_chart3.add(key, all_time_rented_movies[key])

        bar_chart3.render_to_file('/home/bogdan/PycharmProjects/project/script/movies/static/charts/chart3.svg')

    users = User.objects.all()
    movie_id = req.GET.get('idmovie')
    bar_chart4 = pygal.Bar()
    drugo_ime_id = {}
    drugo_ime = {}
    bar_chart4.title = "Broj usera koji su rentirali specificni film"

    if movie_id:
        for transaction in transactions:
            if transaction.rented:
                if transaction.movie_id == int(movie_id):
                    if transaction.user_id not in drugo_ime_id:
                        drugo_ime_id[transaction.user_id] = 1
                    else:
                        drugo_ime_id[transaction.user_id] += 1

        for x in users:
            for temp in drugo_ime_id:
                if x.id == temp:
                    drugo_ime[x.username] = drugo_ime_id[temp]

        for key in drugo_ime:
            bar_chart4.add(key, drugo_ime[key])

        bar_chart4.render_to_file('/home/bogdan/PycharmProjects/project/script/movies/static/charts/chart4.svg')

    return render(req, 'chart.html')
