from django.contrib.postgres.fields import ArrayField
from django.db import models


class CinemaRoom(models.Model):
    name = models.CharField(max_length=50)
    films = models.ManyToManyField('film.Move')
    column = models.IntegerField(default=10)
    row = models.IntegerField(default=10)
    seating = ArrayField(
        ArrayField(
            models.BooleanField(blank=True),
        ),
        blank=True
    )

    def __str__(self):
        return self.name
