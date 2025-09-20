from django.shortcuts import get_object_or_404, render , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post , Comment , Reaction
from django.utils.crypto import get_random_string
# Create your views here.


def community_home(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request , "community_home.html" , {"posts" : posts})


@login_required
def create_post(request):
    if request.method == "POST":
        content = request.POST.get("content")
        category = request.POST.get("category" , "positive")

        #If anonymous logs in , then :
        if "anonymous" in request.POST:
            anon_name = "Guest" + get_random_string(5)
            Post.objects.create(content = content , category = category , anonymous_name = anon_name)

        else :
            Post.objects.create(content = content , category = category , author = request.user)

        messages.success(request , "✅ Post created successfully!")
        return redirect("community_home")
    return render(request , "create_post.html")



@login_required
def add_comment(request , post_id):
    post = get_object_or_404(Post , id = post_id)
    if request.method == "POST":
        content = request.POST.get("content")

        #if anonymously posting...
        if "anonymous" in request.POST:
            anon_name = "Guest" + get_random_string(5)
            Comment.objects.create(post = post , content = content , anonymous_name = anon_name)
        else:
            Comment.objects.create(post = post , content = content , author = request.user)

        return redirect("community_home")
    


@login_required
def like_post(request , post_id):
    post = get_object_or_404(Post , id = post_id)
    already_liked = Reaction.objects.filter(post = post , user = request.user)

    if not already_liked:
        Reaction.objects.create(post = post , user  = request.user , reaction_type = "like")
    
    return redirect("community_home")