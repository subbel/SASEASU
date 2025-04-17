from meetings.models import *

event = "Shark Tank 2.0 S24"

for student in Student.objects.all():
    if event in student.events:
        print(f"{student.fisrtname},{student.lastname},{student.major},{student.email}")
