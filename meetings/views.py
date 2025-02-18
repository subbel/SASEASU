from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.db.models import F
from django.urls import reverse
from .models import Meetings, Event, Student,  Signin
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.template.context_processors import csrf

def meeting_list_view(request):
    queryset = Meetings.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "test.html" ,context)


@csrf_protect
def signin(request):
    dropdown = get_object_or_404(Signin, pk =1)
    event = get_object_or_404(Event, title = dropdown.current)
    context = {}
    context.update(csrf(request))
    context["event"] = event
    reason_for_error = ""
    if request.method == "POST":
        firstname = request.POST["firstname"].strip().capitalize()
        lastname = request.POST["lastname"].strip().capitalize()
        email = request.POST["email"].strip().lower()
        asuid = request.POST["asuid"].strip()
        gradyear = request.POST["graduationyear"].strip()
        discord = request.POST["discord"].strip()
        year = request.POST["year"].strip()
        if(request.POST["major_dropdown"] != "Other"):
            major = request.POST["major_dropdown"].strip()
        else:
            major = request.POST["major"].strip()
        campus = request.POST["campus"].strip()
        context["firstnameactual"] = firstname
        context["lastnameactual"] = lastname
        context["emailactual"] = email
        context["asuidactual"] = asuid
        context["discordactual"] = discord
        context["gradactual"] = gradyear
        context["yearactual"] = year
        context["campusactual"] = campus
        context["majoractual"] = major
        error = False
        if request.POST.get("signup"):
            try:
                student = Student.objects.get(email = email)
                if student.ASUID == asuid:
                    student.update(email, firstname, lastname, asuid, gradyear, discord, year, major, campus,)
                else:
                    raise Exception("asuid was not matching")
            except Student.DoesNotExist:
                student = Student()
                student.signup(email, firstname, lastname, asuid, gradyear, discord, year, major, campus,)
            except:
                error = True
                reason_for_error = "Your Email is registered with us already but your ASUID is incorrect. Thank you :)"
        elif request.POST.get("update"):
            try:
                student = Student.objects.get(email = email)
                if student.ASUID == asuid:
                    student.update(email, firstname, lastname, asuid, gradyear, discord, year, major, campus,)
                else:
                    raise Exception("asuid ws not matching")
            except Student.DoesNotExist:
                error = True
                reason_for_error = "Email is unregistered/incorrect. Thank you :)"
            except:
                error = True
                reason_for_error = "Your Email is correct but your ASUID is incorrect. Thank you :)"
        else:
            try:
                student = Student.objects.get(email = email)
                if student.ASUID == asuid:
                    student.update(email, firstname, lastname, asuid, gradyear, discord, year, major, campus,)
                else:
                    raise Exception("asuid ws not matching")
            except Student.DoesNotExist:
                error = True
                reason_for_error = "Email is unregistered/incorrect. Thank you :)"
            except:
                error = True
                reason_for_error = "Your Email is correct but your ASUID is incorrect. Thank you :)"
        if error == False:
            if student.validprofile == False:
                checking = student.cleanup(email, firstname, lastname, asuid, gradyear, discord, year, major, campus,)
                if len(checking) != 0:
                    error = True
                    reason_for_error = "Your previous info was found incorrect, please fill out the entire form. Thank you :)"
                    context["updateallinfo"] = "True"
                else:
                    student.validprofile = True
                    student.save()
                    error = False
        if error == False:
            if event.title not in student.events:
                event.attendance = F("attendance") + 1
                event.save()
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
                elif typo == "5":
                    student.Socials +=1
                    student.GBM += 1
                    student.save()
                elif typo == "6":
                    student.Socials +=1
                    student.Industry += 1
                    student.save()
                student.events += event.title + " , "
                student.save()
                context = {}
                return HttpResponseRedirect(reverse("thankyou"))
            elif event.title in student.events:
                return HttpResponseRedirect(reverse("thankyou"))
        else:
            context["error"] = reason_for_error
        if error == True:
            context["error"] = reason_for_error
    return render(request, "signin.html", context)

def eboard_input_view(request):
    meetings = Meetings.objects.all()
    students = Student.objects.all()
    Signing = Signin.objects.all()

    return render(request, "eboard_input.html", context={"meetings" : meetings, "students":students, "signin":Signing})

def thank_view(request):
    return render(request, "sign.html")

def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello World <h1>")
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello World <h1>")
    return render(request, "about.html", {})

def eboard_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello World <h1>")
    return render(request, "eboard.html", {})

def gallery_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello World <h1>")
    return render(request, "gallery.html", {})

def donate_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello World <h1>")
    return render(request, "donate.html", {})

def meetings_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello World <h1>")
    return render(request, "meetings.html", {})
