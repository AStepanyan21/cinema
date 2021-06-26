from django.db import models


class MoveTime(models.Model):
    time = models.TimeField()

    class Meta:
        verbose_name = 'Movie show time'


class Move(models.Model):
    name = models.CharField(max_length=100)
    move_time = models.ManyToManyField(MoveTime)
    movie_cover = models.ImageField(upload_to='film/uploads/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Moves"
