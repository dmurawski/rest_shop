from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path("home/", views.say_hello, name="home"),
]
