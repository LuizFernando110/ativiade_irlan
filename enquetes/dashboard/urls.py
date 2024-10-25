from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashBoard, name='dashboard'),
]


