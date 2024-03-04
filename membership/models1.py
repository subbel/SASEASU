from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth .models import UserManager, PermissionsMixin,AbstractBaseUser

# class Student(models.Model):
#     name=models.CharField(max_length=120)
#     email = models.EmailField()
#     payment_bool = models.BooleanField(default=False)
#     Socials = models.IntegerField()
#     Industry = models.IntegerField()
#     GBM = models.IntegerField()
#     # password =

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid email adress")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def _create_superuser(self, email, password, **extra_fields):
        email = email
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_superuser( email, password, **extra_fields)

class Student(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=120, blank = True, unique = True)
    first_name=models.CharField(max_length=120, blank = True)
    last_name=models.CharField(max_length=120, blank = True )
    email = models.EmailField(blank=True, unique = True)
    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    date_joined = models.DateTimeField(default = timezone.now)
    last_login = models.DateTimeField(blank = True, null = True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_full_name(self):
        name = self.first_name + " " + self.last_name
        return name

    def get_short_name(self):
        return self.first_name



    # payment_bool = models.BooleanField(default=False)
    # Socials = models.IntegerField()
    # Industry = models.IntegerField()
    # GBM = models.IntegerField()
    # password =