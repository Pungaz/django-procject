import pygal
from django.shortcuts import render


def chart(req):
    bar_chart1 = pygal.Pie()
    bar_chart2 = pygal.HorizontalBar()
    bar_chart3 = pygal.Box()
    bar_chart4 = pygal.Bar()
    bar_chart5 = pygal.Line()

    bar_chart1.add('Korisnici', 20)
    bar_chart1.add('Useri', 30)
    bar_chart1.add('Zaposleni', 35)
    bar_chart1.add('Lopovi', 15)

    bar_chart2.add('Fibonacci2', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    bar_chart3.add('Fibonacci3', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    bar_chart4.add('Fibonacci4', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    bar_chart5.add('Fibonacci5', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    bar_chart1.render_to_file('/home/bogdan/PycharmProjects/project/script/movies/static/charts/chart1.svg')
    bar_chart2.render_to_file('/home/bogdan/PycharmProjects/project/script/movies/static/charts/chart2.svg')
    bar_chart3.render_to_file('/home/bogdan/PycharmProjects/project/script/movies/static/charts/chart3.svg')
    bar_chart4.render_to_file('/home/bogdan/PycharmProjects/project/script/movies/static/charts/chart4.svg')
    bar_chart5.render_to_file('/home/bogdan/PycharmProjects/project/script/movies/static/charts/chart5.svg')

    return render(req, 'chart.html')
