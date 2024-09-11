from django.urls import path
from . import views
urlpatterns = [
    path("", views.testPage, name="test-page"),
    path("index",  views.indexPage, name="index"),
    path("about/", views.aboutUs, name="about"),
    path("contact/", views.contactUs),
    path("for/", views.forPage, name="for-page"),
    path("card/", views.cardView, name="card-page"),
    path("color/", views.cardColor, name="card-color"),
    path("forggg/", views.forGGG, name="for-test"),
    path("login/", views.loginPage, name="login-page"),
    path("register/", views.registerPage, name="register-page"),
    path("page2/", views.page2, name='page2'),
]
