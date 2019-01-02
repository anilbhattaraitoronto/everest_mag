from django.shortcuts import render, get_object_or_404
from .models import Post, Album, Video

# Create your views here.
def index(request):
    news_posts = Post.objects.all().filter(post_type='News')
    opinion_posts = Post.objects.all().filter(post_type='Opinion')
    albums = Album.objects.all().filter(is_latest=True)
    upcoming_events = Post.objects.all().filter(post_type='Event')
    videos = Video.objects.all().filter(is_latest=True)
    context={
        'news_posts': news_posts,
        'opinion_posts':opinion_posts,
        'upcoming_events':upcoming_events,
        'albums':albums,
        'videos':videos,
    }
    return render(request, 'posts/index.html', context)
def post(request, post_id):
    post=get_object_or_404(Post, pk=post_id)
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