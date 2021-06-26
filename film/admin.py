from django.contrib import admin

from film.models import Move, MoveTime


@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    pass


@admin.register(MoveTime)
class MoveTimeAdmin(admin.ModelAdmin):
    pass
