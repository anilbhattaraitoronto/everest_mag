from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('news/<int:post_id>', views.news_post, name='news_post'),
    path('opinion/<int:post_id>', views.opinion_post, name='opinion_post'),
    path('event/<int:post_id>', views.event_post, name='event_post'),
    path('news/', views.news, name='news'),
    path('opinion/', views.opinion, name='opinion'),
]
