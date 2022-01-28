from django.urls import path
from .views import *

urlpatterns = [
    path('blog/', blog, name="all_posts"),
    path('topic/<str:topic>', blog, name="topic"),
    path('post/<str:name>', post, name="post"),
    path('about-me/', about_me, name="about_me"),
    path('contact/', contact, name="contact"),
    path('contact/thank-you/', thank_you, name="thank_you"),
    path('', home, name="home")
]