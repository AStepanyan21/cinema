from django.contrib import admin

from cinema_room.forms import CinemaRoomAdminForm
from cinema_room.models import CinemaRoom


@admin.register(CinemaRoom)
class CinemaRoomAdmin(admin.ModelAdmin):
    form = CinemaRoomAdminForm
