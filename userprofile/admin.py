from django.contrib import admin
from .models import Profile , Badge
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display =("user" , "streaks" , "last_active")
    filter_horizontal = ("badges",)



@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ("name" , "description" , "icon")