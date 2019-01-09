from django.shortcuts import render, get_object_or_404
from posts.models import Post, Album, Video, Advert

# Create your views here.
def index(request):
    news_posts = Post.objects.all().filter(post_type='News')[:3]
    opinion_posts = Post.objects.all().filter(post_type='Opinion')[:3]
    albums = Album.objects.all().filter(is_latest=True)
    upcoming_events = Post.objects.all().filter(post_type='Event')[:3]
    videos = Video.objects.all().filter(is_latest=True)[:3]
    advert_set=Advert.objects.all()
    advert1=advert_set.filter(priority='First', is_live=True)
    advert2=advert_set.filter(priority='Second', is_live=True)
    advert3=advert_set.filter(priority='Third', is_live=True)
    advert4=advert_set.filter(priority='Fourth', is_live=True)
    advert5=advert_set.filter(priority='Fifth', is_live=True)
    advert6=advert_set.filter(priority='Sixth', is_live=True)
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
        'advert6':advert6,
    }
    return render(request, 'pages/index.html', context)


    