from meetings.models import *
from django.shortcuts import get_object_or_404

students = Student.objects.all()
events = Event.objects.all()

for event in events:
    counter = 0
    for student in students:
        counter += student.events.count(event.title)
        if student.events.count(event.title) > 1:
            print(student)
    if counter != event.attendance:
        print(event.title)



# exec(open("shellform.py").read())