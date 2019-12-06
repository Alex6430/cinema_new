from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Country(models.Model):
    id_country = models.IntegerField(db_column='ID_country', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'Country'


class Film(models.Model):
    id_film = models.IntegerField(db_column='ID_film', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=50)
    specification = models.TextField(blank=True, null=True)
    duration = models.TimeField()
    rental_start_date = models.DateField(blank=True, null=True)
    rental_end_date = models.DateField(blank=True, null=True)
    id_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='ID_country')  # Field name made lowercase.
    id_style = models.ForeignKey('Style', models.DO_NOTHING, db_column='ID_style')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Film'


class Room(models.Model):
    id_room = models.IntegerField(db_column='ID_room', primary_key=True)  # Field name made lowercase.
    # quantity_of_seats = models.IntegerField()
    number_of_rows = models.IntegerField()
    number_of_seats = models.IntegerField()
    title = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Room'


# class RoomSector(models.Model):
#     id_sector = models.IntegerField(db_column='ID_sector', primary_key=True)  # Field name made lowercase.
#     title = models.CharField(max_length=50, blank=True, null=True)
#     id_room = models.ForeignKey(Room, models.DO_NOTHING, db_column='ID_room')  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'Room_sector'


# class Sale(models.Model):
#     id_sale = models.IntegerField(db_column='ID_sale', primary_key=True)  # Field name made lowercase.
#     field_date_field = models.DateTimeField(db_column='_date_')  # Field renamed because it started with '_'. Field renamed because it ended with '_'.
#     operation = models.CharField(max_length=50, blank=True, null=True)
#     id_ticket = models.ForeignKey('Ticket', models.DO_NOTHING, db_column='ID_ticket')  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'Sale'


class Seance(models.Model):
    id_seance = models.IntegerField(db_column='ID_seance', primary_key=True)  # Field name made lowercase.
    field_date_field = models.DateField(db_column='_date_')  # Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_time_field = models.TimeField(db_column='_time_')  # Field renamed because it started with '_'. Field renamed because it ended with '_'.
    id_film = models.ForeignKey(Film, models.DO_NOTHING, db_column='ID_film')  # Field name made lowercase.
    id_room = models.ForeignKey(Room, models.DO_NOTHING, db_column='ID_room')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Seance'


class Seats(models.Model):
    id_seats = models.AutoField(db_column='ID_seats', primary_key=True)  # Field name made lowercase.
    field_rows_field = models.IntegerField(db_column='_rows_')  # Field renamed because it started with '_'. Field renamed because it ended with '_'.
    seats = models.IntegerField()
    # id_room = models.ForeignKey(Room, models.DO_NOTHING, db_column='ID_room')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Seats'


class Style(models.Model):
    id_style = models.IntegerField(db_column='ID_style', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'Style'


class Busy(models.Model):
    id_busy = models.AutoField(db_column='ID_busy', primary_key=True)  # Field name made lowercase.
    id_seance = models.ForeignKey(Seance, models.DO_NOTHING, db_column='ID_seance')
    id_seats = models.ForeignKey(Seats, models.DO_NOTHING, db_column='ID_seats')
    id_room = models.ForeignKey(Room, models.DO_NOTHING, db_column='ID_room')
    field_bool_field = models.BooleanField(db_column='_bool_',  blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Busy'
        unique_together = (('id_seats', 'id_seance', 'id_room'),)


class Ticket(models.Model):
    id_ticket = models.AutoField(db_column='ID_ticket', primary_key=True)  # Field name made lowercase.
    # paid = models.IntegerField(blank=True, null=True)
    # reservation = models.IntegerField(blank=True, null=True)
    # destroyed = models.IntegerField(blank=True, null=True)
    date_of_sale = models.DateTimeField()
    username = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    id_seance = models.ForeignKey(Seance, models.DO_NOTHING, db_column='ID_seance')  # Field name made lowercase.
    id_seats = models.ForeignKey(Seats, models.DO_NOTHING, db_column='ID_seats')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Ticket'


# class TicketPrice(models.Model):
#     id_ticketPrice = models.IntegerField(db_column='ID_ticketPrice', primary_key=True)
#     price = models.DecimalField(max_digits=19, decimal_places=4)
#     id_sector = models.ForeignKey(RoomSector, models.DO_NOTHING, db_column='ID_sector')  # Field name made lowercase.
#     id_seance = models.ForeignKey(Seance, models.DO_NOTHING, db_column='ID_seance')  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'Ticket_price'
#         unique_together = (('id_sector', 'id_seance'),)
