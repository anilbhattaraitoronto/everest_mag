from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField

class Post (models.Model):
    TYPES = (
        ('News', 'News'),
        ('Editorial', 'Editorial'),
        ('Opinion', 'Opinion'),
        ('Event', 'Event'),
    )
    is_latest=models.BooleanField(default=True)
    post_type = models.CharField(choices=TYPES, default='News', max_length=15)
    post_title = models.CharField(max_length=100)
    post_author = models.CharField(max_length=40, blank=True)
    post_date = models.DateTimeField(verbose_name='Posted Date', blank=True)
    post_photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    content=RichTextField()
    event_date=models.CharField(max_length=50)
    
    def __str__(self):
        return self.post_title

class Album(models.Model):
    is_latest=models.BooleanField(default=True)
    title=models.CharField(max_length=40)
    image_1=models.ImageField( blank=True)
    image_2=models.ImageField( blank=True)
    image_3=models.ImageField( blank=True)
    image_4=models.ImageField( blank=True)
    
    def __str__(self):
        return self.title

class Video(models.Model):
    is_latest=models.BooleanField(default=True)
    title=models.CharField(max_length=20)
    video=models.URLField(verbose_name='Youtube Embed Url in src')
    
    def __str__(self):
        return self.title
    
class Advert(models.Model):
    PRIORITY=(
        ('First', 'First'),
        ('Second', 'Second'),
        ('Third', 'Third'),
        ('Fourth', 'Fourth'),
        ('Fifth', 'Fifth'),
        ('Sixth', 'Sixth'),
    )
    is_live=models.BooleanField(default=False)
    priority=models.CharField(choices=PRIORITY, default='First', max_length=7)
    title=models.CharField(max_length=50)
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description=models.TextField()
    contact_info=models.TextField()

    def __str__(self):
        return self.title
