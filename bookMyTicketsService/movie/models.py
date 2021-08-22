from django.db import models

# Create your models here.


class Hall(models.Model):
    hall_id = models.AutoField(primary_key=True)
    hall_name = models.CharField(max_length=20)
    theatre_name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.theatre_name} - {self.hall_name} - {self.city}"


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    rating = models.FloatField()
    grade = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.movie_name}"


class Show(models.Model):
    show_id = models.AutoField(primary_key=True)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.movie.movie_name} - {self.hall.theatre_name} - {self.start_time} - {self.end_time}"
