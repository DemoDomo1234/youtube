from django import template
from story.models import Story
from django.db.models import Count 

register = template.Library()

@register.simple_tag()
def story_like_count(story):
    likes = Story.objects.filter(id=story.id).aggregate(Count('likes'))
    return likes['likes__count']

@register.simple_tag()
def story_comment_count(story):
    comments = Story.objects.filter(id=story.id).aggregate(Count('comments'))
    return comments['comments__count']

@register.simple_tag()
def story_view_count(story):
    views = Story.objects.filter(id=story.id).aggregate(Count('views'))
    return views['views__count']
