from django.contrib import admin

# Register your models here.
from .models import Meetings, Event, Student, Signin

admin.site.register(Meetings)
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "attendance", "type")
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email")
admin.site.register(Signin)

# admin page experimantal


class MeetingsAdmin(admin.ModelAdmin):
    pass