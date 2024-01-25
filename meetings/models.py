from django.db import models
from django.urls import reverse

# Create your models here.
class Meetings(models.Model):
    Sno      = models.IntegerField()
    title    = models.CharField(max_length = 50)
    Slides   = models.URLField()
    Desc     = models.TextField(blank = False)
    Semester = models.CharField(max_length= 5)

    def get_absolute_url(self):
        return f"/meetings/{self.id}"