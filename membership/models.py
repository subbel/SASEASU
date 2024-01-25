from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=120)
    email = models.EmailField()
    payment_bool = models.BooleanField(default=False)
    Socials = models.IntegerField()
    Industry = models.IntegerField()
    GBM = models.IntegerField()
    # password =
