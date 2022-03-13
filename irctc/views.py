from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import uuid
from .models import *
import json
from irctc.seat_manage import manage_seat
from .constants import *
# Create your views here.

#admin
#user
#book seats
#see list of seats
#book seat with preferences
@api_view(['POST'])
def admin_add_train_to_irctc(request):
    res={}
    train_name=request.data.get("train_name","")
    print(train_name)
    if Train.objects.filter(train_name=train_name).exists():
        res['status']="train with this name already exists"
        return Response(res)
    train_code=uuid.uuid4()
    train_obj=Train()
    train_obj.train_name=train_name
    train_obj.train_code=train_code
    train_obj.save()
    print(train_obj.id)
    res["status"]="success"
    res["name"]=train_name
    return Response(res)

@api_view(['POST'])
def admin_add_coach_to_train(request):
    res={}
    coach_type=request.data['coach_type']
    train_id = request.data['train_id']
    coach_code = uuid.uuid4()
    if Train.objects.filter(id=train_id).first() is None:
        res["status"]="failed"
        res["message"]="train does not exist"
        return Response(res)
    coach_obj=TrainCoach()
    coach_obj.coach_type=coach_type
    coach_obj.train=Train.objects.filter(id=train_id).first()
    coach_obj.coach_code=coach_code
    coach_obj.save()
    res["status"]="success"
    res["message"]="coach created successfully"
    return Response(res)

@api_view(['POST'])
def admin_remove_coach_of_train(request):
    res={}
    coach_id=request.data['coach_id']
    if TrainCoach.objects.filter(id=coach_id).first() is None:
        res["status"]="failed"
        res["message"]="coach does not exist"
        return Response(res)
    coach_obj=TrainCoach.objects.filter(id=coach_id).first()
    coach_obj.delete()
    res["status"]="delete success"
    return Response(res)

@api_view(['POST'])
def admin_update_coach_of_train(request):
    res={}
    coach_id=request.data['coach_id']
    coach_type=request.data['coach_type']
    if TrainCoach.objects.filter(id=coach_id).first() is None:
        res["status"]="failed"
        res["message"]="coach does not exist"
        return Response(res)
    coach_obj=TrainCoach.objects.filter(id=coach_id).first()
    coach_obj.coach_type=coach_type
    coach_obj.save()
    res["status"]="update success"
    return Response(res)

@api_view(['POST'])
def view_all_seats_in_coach_of_train(request):
    res={}
    coach_id=request.data['coach_id']
    if TrainCoach.objects.filter(id=coach_id).first() is None:
        res["status"]="failed"
        res["message"]="coach does not exist"
        return Response(res)
    coach_obj=TrainCoach.objects.filter(id=coach_id).first()
    all_seats=Seat.objects.filter(coach=coach_obj)
    print(len(all_seats))
    all_seats=[]
    for seat in all_seats:
        seat=manage_seat(seat)
        seat_dict={
            "seat_id":seat.id,
            "seat_number":seat.seat_number,
            "seat_booking_status":seat.booking_status,
            "seat_type":seat.seat_type
        }
        all_seats.append(seat_dict)
    res["status"]="success"
    res["seats_details"]=all_seats
    return Response(res)

@api_view(['POST'])
def user_admin_view_available_seats_of_coach(request):
    res={}
    coach_id=request.data['coach_id']
    if TrainCoach.objects.filter(id=coach_id).first() is None:
        res["status"]="failed"
        res["message"]="coach does not exist"
        return Response(res)
    coach_obj=TrainCoach.objects.filter(id=coach_id).first()
    all_seats_available=Seat.objects.filter(coach=coach_obj,booking_status=False) #seats booking not done
    print(len(all_seats_available))
    seats_available=[]
    for seat in all_seats_available:
        seat=manage_seat(seat)
        seat_dict={
            "seat_id":seat.id,
            "seat_number":seat.seat_number,
            "seat_booking_status":seat.booking_status,
            "seat_type":seat.seat_type
        }
        seats_available.append(seat_dict)
    res["status"]="success"
    res["seats available"]=seats_available
    return Response(res)

@api_view(['POST'])
def book_single_seat_incoach(request):
    res={}
    coach_id=request.data['coach_id']
    seat_id=request.data['seat_id']
    if TrainCoach.objects.filter(id=coach_id).first() is None:
        res["status"]="failed"
        res["message"]="coach does not exist"
        return Response(res)
    booking_obj=Booking()
    fare=FARE
    pnr_number=uuid.uuid4()
    booking_station_details=FROM_STATION + "-" + TO_STATION
    seat_booked=Seat.objects.filter(id=seat_id).first()
    booking_obj.fare=fare
    booking_obj.pnr_number=pnr_number
    booking_obj.booking_station_details=booking_station_details
    booking_obj.seat_booked=seat_booked
    booking_obj.save()
    booking_dict={
        "fare":fare,
        "pnr_number":pnr_number,
        "booking_station_details":booking_station_details,
        "seat_booked":seat_booked.seat_number,
        "booking_status":seat_booked.booking_status
    }
    res["status"]="success"
    res["booking details"]=booking_dict
    return Response(res)


@api_view(['POST'])
def book_multiple_seat_in_different_coach(request):
    res={}
    booking_data=request.data['booking_data']
    booking_details=[]
    for booking in booking_data:
        seat_id=booking['seat_id']
        coach_id=booking['coach_id']
        if Seat.objects.filter(id=coach_id,coach=coach_id,booking_status=False).first() is None:
            booking["status"]="not available"
            booking_details.append(booking)
        booking_obj=Booking()
        fare=FARE
        pnr_number=uuid.uuid4()
        booking_station_details=FROM_STATION + "-" + TO_STATION
        seat_booked=Seat.objects.filter(id=seat_id).first()
        booking_obj.fare=fare
        booking_obj.pnr_number=pnr_number
        booking_obj.booking_station_details=booking_station_details
        booking_obj.seat_booked=seat_booked
        booking_obj.save()
        booking["status"]={
            "fare":fare,
            "pnr_number":pnr_number,
            "booking_station_details":booking_station_details,
            "seat_booked":seat_booked.seat_number,
            "booking_status":seat_booked.booking_status
        }
        booking_details.append(booking)
    res['details']=booking_details
    return Response(res)