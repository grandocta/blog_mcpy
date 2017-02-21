from django import template
from django.utils import timezone
from index.models import Topic
register = template.Library()

@register.simple_tag
def topicCount():
	numTopics = Topic.objects.filter(published_date__lte=timezone.now()).count()
	return numTopics