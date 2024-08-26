from django.db import models
from django import forms
from django.urls import reverse

type = {"GBM": 1, "Social" : 2, "Industry Event" : 3}

Type_CHOICES = (
    ('1','GBM'),
    ('2', 'Social'),
    ('3','Industry Event'),
    ('4', 'Industry and GBM'),
    ('5', 'Social and GBM'),
    ('6', 'Social and Industry'),
    ('None', 'None'),
)

Semester = (
    ('Fall', 'Fall'),
    ('Spring', 'Spring'),
    ('Summer', 'Summer'),
    ('None', 'None'),
)

Year = (
    ('Freshman', 'Freshman'),
    ('Sophomore', 'Sophomore'),
    ('Junior', 'Junior'),
    ('Final', 'Final'),
    ('Grad', 'Grad'),
)

Major = (
    ('Aerospace Engineering', 'Aerospace Engineering'),
    ('Biomedical Engineering', 'Biomedical Engineering'),
    ('Chemical Engineering', 'Chemical Engineering'),
    ('Computer Science', 'Computer Science'),
    ('Computer Systems', 'Computer Systems'),
    ('Electrical Engineering', 'Electrical Engineering'),
    ('Engineering Management', 'Engineering Management'),
    ('Environmental Engineering', 'Environmental Engineering'),
    ('Graphic Information Technology', 'Graphic Information Technology'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
    ('Software Engineering', 'Software Engineering'),
    ('Materials Science & Engineering', 'Materials Science & Engineering'),
    ('Other', 'Other'),
)

Campus = (
    ('Tempe', 'Tempe'),
    ('West', 'West'),
    ('Downtown', 'Downtown'),
    ('Poly', 'Poly'),
    ('Havasu', 'Havasu'),
)

class Event(models.Model):
    title = models.CharField(max_length=100)
    attendance = models.IntegerField(default=0)
    type = models.CharField(max_length=20, choices= Type_CHOICES, default= 'None')
    date = models.DateTimeField()
    flyer = models.ImageField(upload_to="static/Flyers/")

    def __str__(self) -> str:
        return self.title

class Student(models.Model):
    firstname = models.CharField(blank=False, max_length = 50)
    lastname = models.CharField(blank = False, max_length = 50)
    email = models.CharField(max_length=100)
    ASUID = models.CharField(max_length=10)
    Socials = models.IntegerField(default=0)
    GBM = models.IntegerField(default=0)
    Industry = models.IntegerField(default=0)

    graduation_year = models.CharField(max_length=50)
    discord = models.CharField(max_length=50)
    year = models.CharField(max_length=20, choices=Year)
    major = models.CharField(max_length=100,)
    campus = models.CharField(max_length=50, choices=Campus)

    def __str__(self) -> str:
        return self.firstname + " " + self.lastname

    @classmethod
    def create(cls, firstname, lastname, year, email):
        cls(firstname = firstname)
        cls(lastname = lastname)
        cls(year = year)
        cls(email = email)
        return cls




class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['Socials', 'GBM', 'Industry']

class Meetings(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title    = models.CharField(max_length = 50)
    Slides   = models.URLField()
    Desc     = models.TextField(blank = False)
    Semester = models.CharField(max_length= 10, choices=Semester, default='None')

    class Meta:
        verbose_name_plural = "Meetings"

    def __str__(self) -> str:
        return self.title

class Signin(models.Model):
    current = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Signin"