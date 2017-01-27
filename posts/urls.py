from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^create/', views.create, name="create"),
    url(r'(?P<pk>\d+)/upvote', views.upvote, name="upvote"),
    url(r'(?P<pk>\d+)/downvote', views.downvote, name="downvote"),
]
