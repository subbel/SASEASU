from meetings.models import *
from django.shortcuts import get_object_or_404

students = Student.objects.all()
events = Event.objects.all().order_by('date')

industry = []
for event in events:
    print(event.title, " Attendance : ", event.attendance)


# exec(open("shellform.py").read())