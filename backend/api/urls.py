from django.contrib import admin
from django.urls import path

from api import views


urlpatterns = [
    path('frames/', views.frame_view),
    path('forks/', views.fork_view),
    path('cranksets/', views.crankset_view),
    path('cassettes/', views.cassette_view),
    path('frontderailleurs/', views.front_derailleur_view),
    path('rearderailleurs/', views.rear_derailleur_view),
    path('brakes/', views.brake_view),
    path('brakelevers/', views.brake_lever_view),
    path('derailleurlevers/', views.derailleur_lever_view),
    path('rotors/', views.rotor_view),
    path('handlebars/', views.handlebar_view),
    path('stems/', views.stem_view),
    path('saddles/', views.saddle_view),
    path('seatposts/', views.seatpost_view),
    path('wheels/', views.wheels_view),
    path('bikeparts/', views.bikepartsView.as_view()),
]
