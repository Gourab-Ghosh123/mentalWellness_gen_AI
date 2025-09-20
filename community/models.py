from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid.uuid4 , editable=False)
    author = models.ForeignKey(User , on_delete=models.SET_NULL , null = True , blank = True)
    anonymous_name = models.CharField(max_length=50 , default = "Anonymous🌸")
    category = models.CharField(
        max_length=50 ,
        choices=[
            ("positive" ,"Postive Thoughts"),
            ("coping" , "Coping Tips"),
            ("gratitude" , "Daily Gratitude"),
        ],
        default="positive"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:30]
    


class Comment(models.Model):
    post = models.ForeignKey(Post , related_name="comments" , on_delete=models.CASCADE)
    author = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank=True)
    anonymous_name = models.CharField(max_length=50 , default="Anonymous")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



class Reaction(models.Model):
    post = models.ForeignKey(Post , related_name = "reactions" , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    reaction_type = models.CharField(max_length=20 , choices=[("like" , "Like")])
    created_at = models.DateTimeField(auto_now_add=True)


class Report(models.Model):
    post = models.ForeignKey(Post , related_name = "reports" , on_delete=models.CASCADE)
    reporter = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank=True)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)