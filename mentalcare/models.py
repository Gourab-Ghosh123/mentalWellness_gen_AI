from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ChatMessage(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name= 'messages')
    message = models.TextField() # The user's mesage
    response = models.TextField(blank=True , null = True)  # The Bot's message
    timestamp = models.DateTimeField(auto_now_add = True)  #When the message was sent


    def __str__(self):
        return f"{self.user.username} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
    


class MoodSlider(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    mood_value = models.IntegerField()  # 1 to 10 scale...
    date = models.DateTimeField(auto_now_add=True)

    def get_emoji(self):
        if self.mood_value <= 3 :
            return "😢"
        elif self.mood_value >= 4 and self.mood_value <= 7:
            return "😐"
        elif self.mood_value >= 8:
            return "🙂"
        return "🤩"


    def __str__(self):
        return f"{self.user.username} - {self.mood_value} on ({self.date})"