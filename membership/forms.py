from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Student

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Student
        fields = ("username", "email", "name",)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Student
        fields = ("username", "email", 'name', 'Socials', 'Industry', 'GBM',)