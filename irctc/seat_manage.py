
from .models import *

def manage_seat(seat_obj):
    id=seat_obj.id
    if id%3==0:
        seat_obj.seat_type="LOWER-BIRTH"
    if id%3==1:
        seat_obj.seat_type="MIDDLE-BIRTH"
    if id%3==2:
        seat_obj.seat_type="UPPER-BIRTH"
    seat_obj.seat_number=seat_obj.seat_type+"-"+str(id)
    seat_obj.save()
    return seat_obj