from django.urls import path
from . import views

urlpatterns = [
    path('search/city/<str:city_name>', views.search_movie_by_city),
    path('search/shows/<int:movie_id>', views.search_show_by_movie)
]