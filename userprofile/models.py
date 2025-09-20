from django.db import models
from django.contrib.auth.models import User
from datetime import date , timedelta

# Create your models here.


class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100 , blank=True) #emojis works too...

    def __str__(self):
        return self.name
    


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    streaks = models.IntegerField(default = 0)
    last_active = models.DateField(null = True , blank = True)
    badges = models .ManyToManyField(Badge , blank = True)


    def update_streak(self):
        today = date.today()
        if self.last_active == today:
            return
        elif self.last_active == today - timedelta(days= 1): #Checks if the user was last active yesterday , so its continuous haha!
            self.streaks += 1
        else:
            self.streaks = 1  #who broke the streak , streak gets back to start 1....
        self.last_active = today
        self.save()
        self.check_badges() #checks after updating streaks

    

    def check_badges(self):
        #assigns badges based on streaks...
        streak_badges ={
            3: "Consitency Starter 🌱",
            7: "Weekly Warrior  🔥",
            30: "Monthly Master  👑"
        }
        
        for streak , badge_name in streak_badges.items():
            if self.streaks >= streak:
                badge = Badge.objects.filter(name = badge_name).first()
                if badge and badge not in self.badges.all():
                    self.badges.add(badge)