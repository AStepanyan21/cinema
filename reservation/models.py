from django.db import models


class Reservation(models.Model):
    client_name = models.CharField(max_length=50)
    cinema_room = models.ForeignKey('cinema_room.CinemaRoom', on_delete=models.CASCADE)
    armored_row = models.IntegerField()
    armored_chair = models.IntegerField()

    def __str__(self):
        return self.client_name

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        from cinema_room.models import CinemaRoom

        room = CinemaRoom.objects.get(pk=self.cinema_room_id)
        room.seating[self.armored_row - 1][self.armored_chair - 1] = True
        room.save()
        super().save(force_insert, force_update, *args, **kwargs)
