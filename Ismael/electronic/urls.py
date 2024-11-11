
from django.urls import path
from Ismael import views

urlpatterns = [
     path('', views.home, name="home"),
]
