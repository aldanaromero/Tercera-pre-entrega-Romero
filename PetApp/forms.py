from django import forms


class Appointment(forms.Form):
    pet_name = forms.CharField(max_length=40)
    pet_age = forms.IntegerField()
    pet_type = forms.CharField(max_length=40)  # Corregido: se cambió pet_type a type
    owner_name = forms.CharField(max_length=40)
    owner_last_name = forms.CharField(max_length=40)
    owner_mail = forms.EmailField()
    date = forms.DateField()
    medical_specialty = forms.CharField(max_length=40)

