from django.contrib import admin
from cinema_theater.models import *

admin.site.register(Ticket)
admin.site.register(Country)
# admin.site.register(TicketPrice)
# admin.site.register(Sale)
admin.site.register(Seance)
admin.site.register(Seats)
admin.site.register(Style)
admin.site.register(Room)
# admin.site.register(RoomSector)
admin.site.register(Film)
admin.site.register(Busy)


