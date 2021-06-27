import json

from django.http import HttpResponse
from django.template import loader

from cinema_room.models import CinemaRoom
from film.models import Move
from reservation.models import Reservation


def seat_reservation(request, room_name, pk):
    room = CinemaRoom.objects.get(name=room_name)

    if request.method == 'POST':
        body = json.loads(request.body)
        row = int(body['row'])
        column = int(body['column'])
        reservation = Reservation(cinema_room=room, armored_row=row, armored_chair=column)
        reservation.save()

    seating = room.seating
    room_column = range(1, room.column + 1)
    room_row = range(1, room.row + 1)
    data = zip(room_row, seating)
    film = Move.objects.get(pk=pk)
    template = loader.get_template('reservation/index.html')
    context = {
        'room': room,
        'film': film,
        'room_column': room_column,
        'room_row': room_row,
        'seating': seating,
        'data': data
    }
    return HttpResponse(template.render(context, request))
