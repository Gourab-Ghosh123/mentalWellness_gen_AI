from django.urls import path
from . import views




urlpatterns = [
    path("progress_tracker/", views.progress_tracker, name="progress_tracker"),
]
