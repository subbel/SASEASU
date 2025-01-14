from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.db.models import F
from django.core.mail import send_mail
from django.urls import reverse
from .models import Meetings, Event, Student, StudentForm, Signin
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
    if request.method == "POST":
        firstname = request.POST["firstname"].strip().capitalize()
        lastname = request.POST["lastname"].strip().capitalize()
        email = request.POST["email"].strip()
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
        try:
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
            error = False
            student = Student.objects.get(email = request.POST["email"])
            if event.title in student.events:
                return HttpResponseRedirect(reverse("thankyou"))
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
                if asuid!= student.ASUID:
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
                emaildropdown = get_object_or_404(Signin, pk =2)
                emailevent = get_object_or_404(Event, title = emaildropdown.current)
                oldstudents = ""
                newstudents = ""
                x=1
                list = Student.objects.all()
                for i in list:
                    if emailevent.title in i.events:
                        if request.POST.get("signup"):
                            newstudents += i.firstname + "\t"+i.lastname + "\t" + i.email + "\t" + i.major + "\t" + i.ASUID + "\t" + i.discord + "\t" + i.year + "\t" + i.campus + "\t" + i.graduation_year +  "\n"
                        else:
                            oldstudents += i.firstname + "\t"+i.lastname + "\t" + i.email + "\t" + i.major + "\n"
                send_mail(
                    "GBM Data",
                    oldstudents + "\n\n" + newstudents,
                    "saseasuwebmaster@gmail.com",
                    ["saseasuwebmaster@gmail.com"],
                    fail_silently=False,
                )
                return HttpResponseRedirect(reverse("thankyou"))

            else:
                # context["email"] = email
                context["update"] = "update button"
        except(Student.DoesNotExist):
            context["error"] = "Email doesnt exist"
            context["email"] = request.POST["email"]
        except(Student.MultipleObjectsReturned):
            list = Student.objects.filter(email = request.POST["email"])
            for i in list[1:]:
                if i.email == request.POST["email"]:
                    i.delete()
            return HttpResponseRedirect(reverse("thankyou"))
    # request.POST[email] = "hello@asu.edu"
    return render(request, "signin.html", context)

def thank_view(request):
    return render(request, "sign.html")

def download(request, id):
    response = FileResponse(open("../../Students.xlsx", 'rb'))
    return response
