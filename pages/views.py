from django.shortcuts import render, get_object_or_404
from posts.models import Post, Album, Video, Advert

# Create your views here.
def index(request):
    news_posts = Post.objects.all().filter(post_type='News')[:3]
    opinion_posts = Post.objects.all().filter(post_type='Opinion')[:3]
    editorial_posts = Post.objects.all().filter(post_type='Editorial')[:1]
    albums = Album.objects.all().filter(is_latest=True)
    upcoming_events = Post.objects.all().filter(post_type='Event')[:3]
    videos = Video.objects.all().filter(is_latest=True)[:3]
    context={
        'news_posts': news_posts,
        'opinion_posts':opinion_posts,
        'upcoming_events':upcoming_events,
        'albums':albums,
        'videos':videos,
    }
    return render(request, 'pages/index.html', context)


    