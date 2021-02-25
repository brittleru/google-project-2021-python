from django.urls import re_path
from . import views

app_name = 'forums'

urlpatterns = [
    re_path(r"^$", views.ListForums.as_view(), name="all"),
    re_path(r"^new/$", views.CreateForum.as_view(), name="create"),
    re_path(r"^posts/in/(?P<slug>[-\w]+)/$", views.SingleForum.as_view(), name="single"),
    re_path(r"^join/(?P<slug>[-\w]+)/$", views.JoinForum.as_view(), name="join"),
    re_path(r"^leave/(?P<slug>[-\w]+)/$", views.LeaveForum.as_view(), name="leave"),
]
