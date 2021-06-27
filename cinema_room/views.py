from django.http import HttpResponse
from django.template import loader

from cinema_room.models import CinemaRoom


def index(request):
    rooms = CinemaRoom.objects.all()
    template = loader.get_template('cinema_room/index.html')
    context = {
        'rooms': rooms,
    }
    return HttpResponse(template.render(context, request))


def room_timesheet(request, room_name):
    room = room_name
    timesheet = CinemaRoom.objects.get(name=room_name)
    films = timesheet.films.all()
    template = loader.get_template('cinema_room/timesheet.html')
    context = {
        'room': room,
        'films': films,
    }
    return HttpResponse(template.render(context, request))


