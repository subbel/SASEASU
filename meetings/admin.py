from django.contrib import admin
import xlsxwriter
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from meetings.models import Tester

# Register your models here.
from .models import Meetings, Event, Student, Signin


admin.site.register(Meetings)
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "attendance", "type")
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email", "GBM", "Socials", "Industry", "validprofile")

    def mark(modeladmin, request, queryset):
        dropdown = get_object_or_404(Signin, pk =2)
        event = get_object_or_404(Event, title = dropdown.current)
        stringcsv = []
        x=1
        for i in queryset:
            if event.title in i.events:
                stringcsv.append([i.firstname,i.lastname,i.email , i.major])
        response = render(request, "test01.html", context={"data":stringcsv})
        return response
    def active(modeladmin, request, queryset):
        list_of_active = []
        for student in queryset:
            if (student.Socials >= 1 or student.Volunteering >= 1) and (student.Industry >= 1) and (student.GBM >= 1):
                list_of_active.append([student.firstname, student.lastname, student.email, student.major])
        return render(request, "test01.html", context={"data":list_of_active})

    actions = [mark, active]
admin.site.register(Signin)

class MeetingsAdmin(admin.ModelAdmin):
    pass