# Generated by Django 2.2.4 on 2019-08-31 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netapp', '0005_movies_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='imdbRating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='imdbVotes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
