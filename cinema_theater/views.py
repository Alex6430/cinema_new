from django.shortcuts import render
from cinema_theater.models import *
from datetime import *
from django.shortcuts import render, redirect


def admin(request):
    return render(request, 'admin')


def ticket(request, id):
    args = {}
    args['price'] = (Seance.objects.all().filter(id_film=id))
    args['name'] = Film.objects.get(id_film=id).title
    # return render(request, ListView.as_view(queryset=Country.objects.all()[:6],
    #                  template_name='cinema_theater/ticket.html'))
    # list = Seance.objects.all().filter(id_film=id)
    # print(list)
    print(args)
    return render(request, 'cinema_theater/ticket.html', {'args': args})


def seance(request, id_room, id_seance):
    print(id_room)
    print(id_seance)
    print(Room.objects.all().filter(id_room=id_room))
    args = {}
    mas_rows = []
    mas_cols = []
    # mas_seat = [[0]*Room.objects.get(id_room=id_room).number_of_seats]*Room.objects.get(id_room=id_room).number_of_rows
    mas_seat = [[0] * Room.objects.get(id_room=id_room).number_of_seats for i in range(Room.objects.get(id_room=id_room).number_of_rows)]
    id_seats_mass = []
    args['seance'] = id_seance
    args['name'] = Room.objects.get(id_room=id_room).title
    # args['rows'] = range(0,Room.objects.get(roomsector__ticketprice__id_seance=id).number_of_rows)
    args['rows'] = range(1, Room.objects.get(id_room=id_room).number_of_rows + 1)
    args['cols'] = range(1, Room.objects.get(id_room=id_room).number_of_seats + 1)
    args['room'] = id_room
    args['bool_seat'] = []
    args['bool_seat_free'] = []
    for i in Busy.objects.all().filter(id_room=id_room, id_seance=id_seance, field_bool_field=1).values_list(
            'id_seats'):
        for j in i:
            id_seats_mass.append(j)
    print(id_seats_mass)
    for k in id_seats_mass:
        for i in Seats.objects.all().filter(id_seats=k).values_list('field_rows_field'):
            # print(i['field_rows_field'],i['seats'])
            for j in i:
                mas_rows.append(j)
            # mas_cols.append(i['seats'])

        args['bool_rows'] = mas_rows
    # for i in range(0, len(mas_rows)):
    #     args['bool_seat'].append([mas_rows[i], mas_cols[i]])
        for i in Seats.objects.all().filter(id_seats=k).values_list('seats'):
            for j in i:
                mas_cols.append(j)
        args['bool_cols'] = mas_cols

    for k in id_seats_mass:
        for i in Seats.objects.all().filter(id_seats=k).values('field_rows_field','seats'):
            print(i['field_rows_field'], i['seats'])
            # for j in i:
            args['bool_seat'].append([i['field_rows_field'], i['seats']])

    # for i in range(1, len(args['rows'])+1):
    #     args['bool_seat_free'].append(args['rows'][i])
    #     for j in range(0, len(args['cols'])):
    #         args['bool_seat_free'][i].append(args['cols'][j])
    # a=1
    # b=3
    # if [a,b] in
    # print(args['bool_seat_free'])
    for i in range(len(mas_seat)):
        for j in range(len(mas_seat[i])):
            # print(mas_seat[i][j])
            mas_seat[i][j] = j+1
            for k in args['bool_seat']:
                if i==k[0] and j==k[1]:
                    mas_seat[i-1][j-1] = 0

            # print(i,j)
            # mas_seat[i - 1][j - 1] = j
            # print(mas_seat[i-1][j-1])
    for i in range(len(mas_seat)):
        args['bool_seat_free'].append([i+1,mas_seat[i]])


    print(args['bool_seat'])
    print(args['bool_seat_free'])
    # print(args['bool_rows'], args['bool_seat'],args['bool_seat_free'])
    return render(request, 'cinema_theater/seance.html', {'args': args})


def pay(request, row, seat, id_room, id_seance, id_user):
    print(row, seat, id_room, id_seance)
    args = {}
    args['seance_date'] = Seance.objects.get(id_seance=id_seance).field_date_field
    args['seance_time'] = Seance.objects.get(id_seance=id_seance).field_time_field
    args['film'] = Film.objects.get(seance__id_seance=id_seance).title
    args['room'] = Room.objects.get(id_room=id_room).title
    args['room_id'] = id_room
    args['seance_id'] = id_seance
    args['row'] = row
    args['seat'] = seat
    Seats.objects.create(field_rows_field=row, seats=seat)
    id_seats = Seats.objects.all().values('id_seats').last()
    print(id_seats['id_seats'])
    # Ticket.objects.create(id_seats=id_seats , id_seance= id_seance,username_id='admin')
    Busy.objects.create(id_seats=Seats.objects.get(id_seats=id_seats['id_seats']),
                        id_seance=Seance.objects.get(id_seance=id_seance), id_room=Room.objects.get(id_room=id_room),
                        field_bool_field=1)
    Ticket.objects.create(id_seance=Seance.objects.get(id_seance=id_seance),
                          id_seats=Seats.objects.get(id_seats=id_seats['id_seats']),
                          username_id=User.objects.get(id=id_user).id,
                          date_of_sale=datetime.now())
    args['busy'] = Busy.objects.all().values('id_busy').last()['id_busy']
    print(args)
    return render(request, 'cinema_theater/pay.html', {'args': args})


def bin(request, id_user):
    print(id_user)
    args = {}
    args['film'] = []
    args['row'] = []
    args['seat'] = []
    args['date_seance'] = []
    args['time_seance'] = []
    args['seance'] = []
    args['seats'] = []
    args['dic'] = []
    id_seance = Ticket.objects.all().filter(username=id_user).values('id_seance', 'id_seats','id_ticket')

    for i in id_seance:
        args['film'].append(Film.objects.get(seance__id_seance=i.get('id_seance')).title)
        args['date_seance'].append(Seance.objects.get(id_seance=i.get('id_seance')).field_date_field)
        args['time_seance'].append(Seance.objects.get(id_seance=i.get('id_seance')).field_time_field)
        args['row'].append(Seats.objects.get(id_seats=i.get('id_seats')).field_rows_field)
        args['seat'].append(Seats.objects.get(id_seats=i.get('id_seats')).seats)
        args['seance'].append(i.get('id_seance'))
        args['seats'].append(i.get('id_seats'))

    print(id_seance)

    for i in range(0, len(args['film'])):
        args['dic'].append([args['film'][i], args['date_seance'][i],  args['time_seance'][i],
                    args['row'][i], args['seat'][i], args['seance'][i],args['seats'][i]])

    print(args['dic'])

    return render(request, 'cinema_theater/bin.html', {'args': args})


def delite(request, id_seance, id_seats, id_user):
    print(id_seance,id_seats)
    Ticket.objects.filter(id_seance=id_seance,id_seats=id_seats).delete()
    Busy.objects.filter(id_seance=id_seance,id_seats=id_seats).update(field_bool_field=0)
    return redirect("/bin/"+id_user)