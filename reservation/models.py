from django.db import models


class Reservation(models.Model):
    cinema_room = models.ForeignKey('cinema_room.CinemaRoom', on_delete=models.CASCADE)
    armored_row = models.IntegerField()
    armored_chair = models.IntegerField()

    def __str__(self):
        return self.cinema_room.name

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.cinema_room.seating[self.armored_row - 1][self.armored_chair - 1] = True
        self.cinema_room.save()
        super().save(force_insert, force_update, *args, **kwargs)
