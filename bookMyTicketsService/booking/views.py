from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import traceback
import json

from .models import Booking, Seat
from user.models import User, Session
from movie.models import Movie, Show, Hall

# Create your views here.


def search_seats_by_show(request, show_id):
    try:
        if request.method != 'GET':
            return JsonResponse({
                'message': 'This method is not allowed'
            }, status=405)
        seats = Seat.objects.filter(show_id=show_id, is_booked=False).values()
        return JsonResponse({
            'seats': list(seats)
        })
    except Exception as e:
        traceback.print_exc()
        return JsonResponse({
            'message': str(e)
        }, status=500)


@csrf_exempt
def book_seats(request, show_id):
    try:
        if request.method != 'POST':
            return JsonResponse({
                'message': 'This method is not allowed'
            }, status=405)
        booking_form = json.loads(request.body)
        # check user is logged in
        session_log = Session.objects.filter(session_id=booking_form['session_id'], is_logged_in=True)
        if session_log.count() == 0:
            return JsonResponse({
                'message': 'Please Log In before booking tickets'
            }, status=401)

        # validate show id
        show = Show.objects.filter(show_id=show_id)
        if show.count() == 0:
            return JsonResponse({
                'message': 'Show not found!'
            }, status=401)

        # book tickets
        new_booking = Booking.objects.create(
            user=session_log[0].user,
            show=show[0],
            num_of_seats=len(booking_form['seats'])
        )
        Seat.objects.filter(
            seat_num__in=booking_form['seats']
        ).update(is_booked=True, booking=new_booking)

        return JsonResponse({
            'message': 'Booking successful!',
            'booking_id': new_booking.booking_id
        })
    except Exception as e:
        traceback.print_exc()
        return JsonResponse({
            'message': str(e)
        }, status=500)
