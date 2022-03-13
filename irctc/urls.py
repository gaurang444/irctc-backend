from django.urls import path
from . import views
urlpatterns = [
    path('yo/', views.hello_world, name='admin-add-train'),
]