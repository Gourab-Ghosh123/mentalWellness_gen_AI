from django.urls import path
from . import views


urlpatterns = [
    path('community/' , views.community_home , name='community_home'),
    path("new_post/", views.create_post , name = 'create_post'),
    path("<uuid:post_id>/comment/" , views.add_comment , name = 'add_comment'),
    path("<uuid:post_id>/ like/" , views.like_post , name = 'like_post'),
]


