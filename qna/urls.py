from django.urls import path
from . import views


urlpatterns = [
    path('questions/', views.questions, name="questions"),
    path('latestquestions/', views.latestquestions, name="latestquestions"),
    path('ask-a-question/', views.askaquestion, name='askaquestion'),
]