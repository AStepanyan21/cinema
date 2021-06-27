from django.contrib import admin
from django.urls import path

from cinema_room import views as cinema_views
from reservation import views as reservation_views

urlpatterns = [
    path('', cinema_views.index),
    path('room/<str:room_name>/', cinema_views.room_timesheet),
    path('room/<str:room_name>/<int:pk>/', reservation_views.seat_reservation),
    path('admin/', admin.site.urls),
]
