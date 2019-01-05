from django.contrib import admin
from .models import Post, Album, Video, Advert

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('post_date', 'post_author', 'post_title', 'post_type')
    list_display_links=('post_title', 'post_type')
    list_filter=( 'post_date', 'post_title', 'post_author')
    list_per_page=25

class AlbumAdmin(admin.ModelAdmin):
    list_display=['title']
    list_display_links=['title']

class VideoAdmin(admin.ModelAdmin):
    list_display=['title']
    list_display_links=['title']

class AdvertAdmin(admin.ModelAdmin):
    list_display=['title']
    list_display_links=['title']

admin.site.register(Post, PostAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Advert, AdvertAdmin)