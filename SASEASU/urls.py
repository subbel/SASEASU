"""SASEASU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from meetings.views import meeting_list_view, signin, thank_view, home_view, about_view, eboard_view, gallery_view, donate_view, meetings_view, eboard_input_view, get_name,create_event

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('about/', about_view),
    path('eboard/', eboard_view),
    path('gallery/', gallery_view),
    path('donate/', donate_view),
    path('meetings/', meetings_view),
    path('signin/', signin, name="signin"),
    path("test/", meeting_list_view),
    path("thanks/", thank_view, name="thankyou"),
    path("secret/", eboard_input_view, name = "secret"),
    path("get-name/", get_name, name="get_name"),
    path("create-event", create_event, name="create_event")
    # path('student/', include('membership.urls'))
    # path("signups/", new_user)
]
