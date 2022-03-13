from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

#admin
#user
#book seats
#see list of seats
#book seat with preferences
@api_view()
def admin_add_train_to_irctc(request):
    return Response({"message": "Hello, world!"})

@api_view()
def admin_add_coach_to_train(request):
    return Response({"message": "Hello, world!"})

@api_view()
def admin_remove_coach_of_train(request):
    return Response({"message": "Hello, world!"})

@api_view()
def admin_update_coach_of_train(request):
    return Response({"message": "Hello, world!"})

@api_view()
def view_all_seats_in_coach_of_train(request):
    return Response({"message": "Hello, world!"})

@api_view()
def user_(request):
    return Response({"message": "Hello, world!"})
