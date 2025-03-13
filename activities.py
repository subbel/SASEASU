from meetings.models import *

Events = Event.objects.all()

for event in Events:
    print(event.title, event.flyer)
    title = input("What Title would you like :")
    if(title == "n"):
        print("empty")
    else:
        event.name = title
        event.save()

# exec(open("activities.py").read())