from django.shortcuts import render, get_object_or_404
from .models import Post, Album, Video, Advert

# Create your views here.
def index(request):
    news_posts = Post.objects.all().filter(post_type='News')[:3]
    opinion_posts = Post.objects.all().filter(post_type='Opinion')[:3]
    albums = Album.objects.all().filter(is_latest=True)
    upcoming_events = Post.objects.all().filter(post_type='Event')
    videos = Video.objects.all().filter(is_latest=True)
    advert1=Advert.objects.all().filter(priority='First', is_live=True)[:1]
    advert2=Advert.objects.all().filter(priority='Second', is_live=True)[:1]
    advert3=Advert.objects.all().filter(priority='Third', is_live=True)[:1]
    advert4=Advert.objects.all().filter(priority='Fourth', is_live=True)[:1]
    advert5=Advert.objects.all().filter(priority='Fifth', is_live=True)[:1]
    advert6=Advert.objects.all().filter(priority='Sixth', is_live=True)[:1]
    context={
        'news_posts': news_posts,
        'opinion_posts':opinion_posts,
        'upcoming_events':upcoming_events,
        'albums':albums,
        'videos':videos,
        'advert1':advert1,
        'advert2':advert2,
        'advert3':advert3,
        'advert4':advert4,
        'advert5':advert5,
        'advert6':advert6
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