from django.urls import path
from . import views

urlpatterns =[
    path("mood_suggestions/" , views.mood_suggestions , name = 'mood_suggestions'),
]