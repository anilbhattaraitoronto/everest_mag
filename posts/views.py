from django.shortcuts import render, get_object_or_404
from .models import Post, Album, Video, Advert

# Create your views here.

def news_post(request, post_id):
    post=get_object_or_404(Post, pk=post_id, post_type='News')
    context ={
        'post':post
    }
    return render(request, 'posts/post.html', context)
def opinion_post(request, post_id):
    post=get_object_or_404(Post, pk=post_id, post_type='Opinion')
    context ={
        'post':post
    }
    return render(request, 'posts/post.html', context)
def event_post(request, post_id):
    post=get_object_or_404(Post, pk=post_id, post_type='Event')
    context ={
        'post':post
    }
    return render(request, 'posts/post.html', context)
def news(request):
    news_posts=Post.objects.all().filter(post_type='News').filter(is_latest=False)
    context={
        'news_posts':news_posts
    }
    return render(request, 'posts/news.html', context)

def opinion(request):
    opinions=Post.objects.all().filter(post_type='Opinion').filter(is_latest=False)
    context={
        'opinions':opinions
    }
    return render(request, 'posts/opinion.html', context)