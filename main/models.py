import datetime

from django.db import models


class Participant(models.Model):
    name = models.CharField(max_length=20)
    birthday = models.DateField()
    role = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/participants")

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo_name = models.CharField(max_length=50, default="Фото")
    photo_id = models.ImageField(upload_to="photos/gallery")

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return self.photo_name


class Album(models.Model):
    title = models.CharField(max_length=50)
    tracks = models.IntegerField(default=0)
    release_date = models.DateField(default=datetime.date.today())
    photo = models.ImageField(upload_to="photos/albums")

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

    def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=50)
    length = models.IntegerField()
    album = models.ForeignKey('Album', on_delete=models.PROTECT)
    audio_track = models.FileField(upload_to="songs/")

    class Meta:
        verbose_name = "Трек"
        verbose_name_plural = "Треки"

    def __str__(self):
        return self.title

# Create your models here.
