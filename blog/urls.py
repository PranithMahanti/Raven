from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("projects", views.projects, name="projects"),
    path("blog", views.blog, name="blog"),
    path("blog/<str:link>/", views.post, name="post"),
]