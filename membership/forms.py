from django import forms
from django.core.exceptions import ValidationError
from .models import Student

class Student_Signup:
    name=forms.CharField()
    email = forms.EmailField()
    payment_bool = forms.BooleanField()
    Socials = forms.IntegerField()
    Industry = forms.IntegerField()
    GBM = forms.IntegerField()

    def clean_name(self):
        name = self.cleaned_data['name']
        return name

    def clean_email(self):
        email  =  self.cleaned_data['email']
        r = Student.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Account already exists")
        return email