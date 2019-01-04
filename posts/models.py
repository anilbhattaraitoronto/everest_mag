from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

class Post (models.Model):
    TYPES = (
        ('News', 'News'),
        ('Editorial', 'Editorial'),
        ('Opinion', 'Opinion'),
        ('Event', 'Event'),
    )
    post_type = models.CharField(choices=TYPES, default='News', max_length=15)
    post_title = models.CharField(max_length=100)
    post_author = models.CharField(max_length=40, blank=True)
    post_date = models.DateTimeField(verbose_name='Posted Date', blank=True)
    post_photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    text_content_1=RichTextField()
    # sub_heading_1=models.CharField(max_length=30, blank=True)
    # post_photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # text_content_2=models.TextField(blank=True)
    # sub_heading_2=models.CharField(max_length=30, blank=True)
    # post_photo_3=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # text_content_3=models.TextField(blank=True)
    # event_date=models.CharField(max_length=60, blank=True)
    is_latest=models.BooleanField(default=True)

    def __str__(self):
        return self.post_title

class Album(models.Model):
    title=models.CharField(max_length=40)
    image_1=models.ImageField( blank=True)
    image_2=models.ImageField( blank=True)
    image_3=models.ImageField( blank=True)
    image_4=models.ImageField( blank=True)
    is_latest=models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    title=models.CharField(max_length=20)
    video=models.URLField(verbose_name='Youtube Embed Url in src')
    is_latest=models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

