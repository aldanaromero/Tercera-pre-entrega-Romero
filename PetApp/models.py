from django.db import models


class PetAppointment(models.Model):
    date = models.DateField()
    medical_specialty = models.CharField(max_length=30)  # Ver si lo puedo tipar
    pet_appointment_id = models.AutoField(primary_key=True)


class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    type = models.CharField(max_length=40)  # Corregido: se cambió pet_type a type
    pet_appointment = models.ForeignKey(PetAppointment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mail = models.EmailField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
