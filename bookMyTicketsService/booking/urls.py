from django.urls import path
from . import views

urlpatterns = [
    path('search/seats/<int:show_id>', views.search_seats_by_show),
    path('book/seats/<int:show_id>', views.book_seats),
]