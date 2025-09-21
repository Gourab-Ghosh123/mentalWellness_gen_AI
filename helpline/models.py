from django.db import models

class Helpline(models.Model):
    CATEGORY_CHOICES = [
        ('mental', 'Mental Health'),
        ('suicide', 'Suicide Prevention'),
        ('child', 'Child Helpline'),
        ('lgbtq', 'LGBTQ+ Support'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
