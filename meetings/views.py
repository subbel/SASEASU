from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from .models import Meetings, Event, Student, StudentForm, Signin

def meeting_list_view(request):
    queryset = Meetings.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "test.html" ,context)

def signin(request):
    #
    #
    # Title of event here
    dropdown = get_object_or_404(Signin, pk =1)
    event = get_object_or_404(Event, title = dropdown.current)
    #
    #
    #
    context = {}
    context["event"] = event
    firsttimer = False
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        asuid = request.POST["asuid"]
        gradyear = request.POST["graduationyear"]
        discord = request.POST["discord"]
        year = request.POST["year"]
        major = request.POST["major"]
        campus = request.POST["campus"]
        context["firstnameactual"] = firstname
        context["lastnameactual"] = lastname
        context["emailactual"] = email
        context["asuidactual"] = asuid
        if request.POST.get("signup"):
            temp_stud = Student()
            temp_stud.email = email
            temp_stud.firstname = firstname
            temp_stud.lastname = lastname
            temp_stud.ASUID = asuid
            temp_stud.graduation_year = gradyear
            temp_stud.discord = discord
            temp_stud.year = year
            temp_stud.major = major
            temp_stud.campus = campus
            temp_stud.save()
        try:
            error = False
            student = Student.objects.get(email = request.POST["email"])
            if request.POST.get("update"):
                student.firstname = firstname
                student.lastname = lastname
                student.ASUID = asuid
            else:
                if firstname != student.firstname:
                    context["firstname"] = firstname
                    error = True
                if lastname != student.lastname:
                    context["lastname"] = lastname
                    error = True
                if asuid != student.ASUID:
                    context["asuid"] = asuid
                    error = True
            if error == False:
                event.attendance = F("attendance") + 1
                event.save()
                # eventevent.type
                typo = event.type
                if typo == "1":
                    student.GBM += 1
                    student.save()
                elif typo == "2":
                    student.Socials += 1
                    student.save()
                elif typo == "3":
                    student.Industry += 1
                    student.save()
                elif typo == "4":
                    student.Industry += 1
                    student.GBM += 1
                    student.save()
                return HttpResponse("Thank you for signing in")

            else:
                # context["email"] = email
                context["update"] = "update button"
        except(Student.DoesNotExist):
            context["error"] = "Email doesnt exist"
            context["email"] = request.POST["email"]
    # request.POST[email] = "hello@asu.edu"
    return render(request, "meetings/signin.html", context)
