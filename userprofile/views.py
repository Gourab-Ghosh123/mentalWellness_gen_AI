from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User

from .models import Profile

@login_required
def progress_tracker(request):
    profile = request.user.profile
    profile.update_streak()

    return render(request , 'progress_tracker.html' , {"profile" : profile})