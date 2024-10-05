from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # This is the root path
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]