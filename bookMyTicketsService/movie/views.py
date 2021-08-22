from django.http import JsonResponse

import traceback
import json

from .models import Movie, Show, Hall
# Create your views here.


def search_movie_by_city(request, city_name):
    try:

        if request.method != 'GET':
            return JsonResponse({
                'message': 'This method is not allowed'
            }, status=405)

        movies = Movie.objects.filter(show__hall__city=city_name).values()
        return JsonResponse({
            'movies': list(movies)
        })
    except Exception as e:
        traceback.print_exc()
        return JsonResponse({
            'message': str(e)
        }, status=500)


def search_show_by_movie(request, movie_id):
    try:
        if request.method != 'GET':
            return JsonResponse({
                'message': 'This method is not allowed'
            }, status=405)

        shows = Show.objects.filter(movie_id=1).values('show_id', 'date', 'start_time', 'end_time', 'movie__movie_name',
                                                       'hall__theatre_name', 'hall__city', 'hall__address')
        return JsonResponse({
            'shows': list(shows)
        })
    except Exception as e:
        traceback.print_exc()
        return JsonResponse({
            'message': str(e)
        }, status=500)