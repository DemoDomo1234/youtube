# Generated by Django 4.1.5 on 2023-12-08 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Short',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('files', models.FileField(upload_to='short')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes_short', to=settings.AUTH_USER_MODEL)),
                ('tag', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('un_likes', models.ManyToManyField(blank=True, related_name='un_likes_short', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_short', to=settings.AUTH_USER_MODEL)),
                ('views', models.ManyToManyField(blank=True, related_name='views_short', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
