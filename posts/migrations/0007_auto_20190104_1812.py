# Generated by Django 2.1.4 on 2019-01-04 07:12

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_text_content_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text_content_2',
        ),
        migrations.AlterField(
            model_name='post',
            name='text_content_1',
            field=tinymce.models.HTMLField(default='Hello'),
        ),
    ]
