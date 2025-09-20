from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('chat/' , views.chat_view , name='chat'),
    path('chat/clear/' , views.clear_chat , name = 'clear_chat'),
    path('mood_slider/' , views.mood_slider_view , name = 'mood_slider'),
    path('about/' , views.about_view , name = 'about'),
]
