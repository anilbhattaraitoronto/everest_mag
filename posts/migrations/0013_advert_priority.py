# Generated by Django 2.1.4 on 2019-01-04 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20190105_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='priority',
            field=models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth')], default='First', max_length=7),
        ),
    ]