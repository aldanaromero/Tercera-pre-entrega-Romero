from django.urls import path
from PetApp import views

urlpatterns = [
    path('', views.appointment),
    path('appointment/', views.appointment),
    path('search/user', views.search_appointment),
    path('search/', views.search),
]
