from django.urls import path
from . import views

urlpatterns = [
    path('helpline/', views.helpline , name = 'helpline'),
]