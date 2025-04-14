from meetings.models import Student, Event
from django.shortcuts import get_object_or_404

def clean_events(student):
    events = student.events
    event_list = events.split(",")
    event_list = list(map(lambda x : x.strip(), event_list))
    new_event_list = list(dict.fromkeys(event_list))
    if new_event_list == event_list:
        return True
    return False

def check_numbers(student):
    events = student.events
    event_list = events.split(",")
    event_list = list(map(lambda x : x.strip(), event_list))
    socials = 0
    gbm = 0
    ind = 0
    vol = 0
    for event in event_list:
        try:
            event_item = get_object_or_404(Event, title = event)
            typo = event_item.type
            if typo == "1":
                gbm += 1
            elif typo == "2":
                socials += 1
            elif typo == "3":
                ind += 1
            elif typo == "4":
                ind += 1
                gbm += 1
            elif typo == "5":
                socials +=1
                gbm += 1
            elif typo == "6":
                socials +=1
                ind += 1
            elif typo == "7":
                vol +=1
            elif typo == "7":
                gbm +=1
        except:
            if (event.strip() != "" and event.strip() != "None"):
                print(f"Error Found: '{event}' gave an HTTP error for {student.firstname}")

    if gbm != student.GBM or socials != student.Socials or vol != student.Volunteering or ind != student.Industry:
        student.GBM = gbm
        student.Socials = socials
        student.Volunteering = vol
        student.Industry = ind
        student.save()
        return False
    return True

def attendance_cleaning():
    for event in Event.objects.all():
        apparent_attendance = 0
        for student in Student.objects.all():
            if event.title in student.events:
                apparent_attendance += 1
        if apparent_attendance != event.attendance:
            event.attendance = apparent_attendance
            event.save()
            print(f"Event {event.title} is not matching")
attendance_cleaning()