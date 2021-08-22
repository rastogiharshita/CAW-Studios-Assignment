from django.db import models
import uuid

from user.models import User
from movie.models import Show
# Create your models here.


class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    num_of_seats = models.IntegerField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.show.movie.movie_name} - {self.show.hall.theatre_name} - {self.num_of_seats}"


class Seat(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat_num = models.CharField(max_length=4)
    seat_type = models.CharField(max_length=20)
    is_booked = models.BooleanField(default=False)
    price = models.FloatField()
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.seat_num} - {self.show.movie.movie_name} - {self.show.hall.hall_name}"
