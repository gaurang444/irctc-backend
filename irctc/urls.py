from django.urls import path
from .views import *
urlpatterns = [
    path('add-train',admin_add_train_to_irctc, name='admin-add-train'),
    path('add-coach',admin_add_coach_to_train, name='admin-add-coach'),
    path('delete-coach',admin_remove_coach_of_train, name='admin-delete-coach'),
    path('update-coach',admin_update_coach_of_train, name='admin-update-coach'),
    path('view-all-seats',view_all_seats_in_coach_of_train, name='view-all-seats'),
    path('view-available-seats',user_admin_view_available_seats_of_coach, name='view-available-seats'),
    path('book-seat',book_single_seat_incoach, name='book-single-seat'),
    path('book-multiple-seats',book_multiple_seat_in_different_coach, name='book-multiple-seats'),
]