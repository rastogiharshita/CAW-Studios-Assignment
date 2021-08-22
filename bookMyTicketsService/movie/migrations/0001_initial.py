# Generated by Django 3.2.5 on 2021-08-22 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('hall_id', models.AutoField(primary_key=True, serialize=False)),
                ('hall_name', models.CharField(max_length=20)),
                ('theatre_name', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('rating', models.FloatField()),
                ('grade', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('show_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.hall')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
    ]