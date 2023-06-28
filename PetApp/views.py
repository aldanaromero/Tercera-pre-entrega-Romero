from django.shortcuts import render

from PetApp.forms import Appointment
from PetApp.models import User, Pet, PetAppointment


def appointment(request):
    if request.method == 'POST':
        form = Appointment(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            pet_appointment = PetAppointment(date=data["date"], medical_specialty=data["medical_specialty"])
            pet_appointment.save()
            print("Pet appointment: ", pet_appointment)

            pet = Pet(name=data["pet_name"], age=data["pet_age"], type=data["pet_type"],
                      pet_appointment=pet_appointment)
            pet.save()
            print("Pet: ", pet)

            owner = User(name=data["owner_name"], last_name=data["owner_last_name"], mail=data["owner_mail"],
                         pet=pet)
            owner.save()
            print("User: ", owner)
            return render(request, "saveAppointment.html")
    else:
        form = Appointment()
    return render(request, "appointment.html", {"form": form})


def search_appointment(request):
    return render(request, "searchAppointment.html")


def search(request):
    if request.GET['pet_name']:
        pet_name = request.GET['pet_name']
        print("Search: ", pet_name)
        pets = Pet.objects.filter(name__icontains=pet_name)
        return render(request, "resultAppointment.html", {"pets": pets, "pet_name": pet_name})
