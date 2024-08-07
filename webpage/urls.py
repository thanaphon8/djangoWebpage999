from django.urls import path
from . import views
urlpatterns = [
    path("",  views.indexPage, name="index"),
    path("about/", views.aboutUs, name="about"),
    path("contact/", views.contactUs),
    path("for/", views.forPage, name="for-page"),
    path("card/", views.cardView, name="card-page"),
]
