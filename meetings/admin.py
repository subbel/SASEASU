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
    list_display = ("title", "attendance", "type")
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email", "GBM", "Socials", "Industry")

    # @admin.action(description="Data from event")
    def mark_(modeladmin, request, queryset):
        dropdown = get_object_or_404(Signin, pk =2)
        event = get_object_or_404(Event, title = dropdown.current)
        stringcsv = []
        x=1
        for i in queryset:
            if event.title in i.events:
                stringcsv.append([i.firstname,i.lastname,i.email , i.major])
        # workbook.close()
        response = render(request, "test01.html", context={"data":stringcsv, "oldpath":"/Students.xlsx"})
        return response
    actions = [mark_]
admin.site.register(Signin)

class MeetingsAdmin(admin.ModelAdmin):
    pass