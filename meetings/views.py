from django.shortcuts import render
from .models import Meetings

def meeting_list_view(request):
    queryset = Meetings.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "test.html" ,context)