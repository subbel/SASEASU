from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Student(AbstractUser):
    payment_bool = models.BooleanField(default = False)
    name=models.CharField(max_length=120, default = "Shang-Chi")
    Socials = models.IntegerField(default = 0)
    Industry = models.IntegerField(default = 0)
    GBM = models.IntegerField(default = 0)


    def __str__(self):
        return self.username
