from django import forms
from .models import Event

class NameForm(forms.Form): 
    your_name = forms.CharField(label="Your name", max_length=50)

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__" #includes all fields