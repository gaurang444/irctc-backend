from django.db import models
from django.utils.timezone import now
from .constants import *
# Create your models here.
#seats
#users
#coaches
#train
#booking

class User(models.Model):
    GENDER = (
        (MALE, "MALE"),
        (FEMALE, "FEMALE"),
        (OTHERS, "OTHERS"),
    )
    ROLES = (
        (ADMIN, "ADMIN"),
        (IRCTC_USER, "IRCTC-USER"),
    )
    user_role=models.CharField(max_length=255, choices=ROLES,default=IRCTC_USER)
    user_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=255, choices=GENDER,blank=True,null=True)
    password = models.CharField(max_length=50)
    age = models.CharField(max_length=50,blank=True,null=True)
    phone = models.CharField(max_length=50,blank=True,null=True)
    email = models.CharField(max_length=50,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Train(models.Model):
    train_name = models.CharField(max_length=50)
    train_code = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TrainCoach(models.Model):
    COACH_TYPE = (
        (AC_COACH, "AC"),
        (NON_AC_COACH, "NON-AC"),
        (SEATER_COACH, "SEATER"),
    )
    coach_type=models.CharField(max_length=255, choices=COACH_TYPE,default=SEATER_COACH)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    coach_code = models.CharField(max_length=100,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Seat(models.Model):
    SEAT_TYPE = (
        (UPPER_BIRTH, "UPPER-BIRTH"),
        (LOWER_BIRTH, "LOWER-BIRTH"),
        (MIDDLE_BIRTH, "MIDDLE-BIRTH"),
    )
    seat_type=models.CharField(max_length=255, choices=SEAT_TYPE,default=LOWER_BIRTH)
    coach=models.ForeignKey(TrainCoach, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=100,blank=True,null=True)
    booking_status= models.BooleanField(default=False,blank=True,null=True)  #false not booked
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def save(self, *args, **kwargs):
    #     if self.id is not None:
    #         id=int(self.id)
    #         q = Seat.objects.get(id=id)
    #         if id%3==0:
    #             q.seat_type="LOWER-BIRTH"
    #         if id%3==1:
    #             q.seat_type="MIDDLE-BIRTH"
    #         if id%3==2:
    #             q.seat_type="UPPER-BIRTH"
    #         q.seat_number=self.seat_type+"-"+str(id)
    #         q.save()
    #         return

class Station(models.Model):
    station_name = models.CharField(max_length=200,blank=True,null=True)
    station_code = models.CharField(max_length=200,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Booking(models.Model):
    BOOKING_STATUS = (
        (CONFIRMED, "CONFIRMED"),
        (CANCELLED, "CANCELLED"),
        (NOT_PAID, "NOT-PAID"),
    )
    fare=models.IntegerField()
    pnr_number=models.CharField(max_length=200,blank=True,null=True)
    booking_station_details=models.CharField(max_length=200,blank=True,null=True)
    seat_booked=models.ForeignKey(Seat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    booking_status=models.CharField(max_length=255, choices=BOOKING_STATUS,default=CONFIRMED)

class RazorPayPayments(models.Model):
    booking=models.ForeignKey(Booking, on_delete=models.CASCADE)
    pay_link=models.CharField(max_length=200,blank=True,null=True)
    rzpay_invoice_id=models.CharField(max_length=200,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    






