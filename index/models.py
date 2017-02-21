from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
import string
import random
import os

def link_generator(size=6, chars=string.ascii_lowercase + string.digits + string.ascii_uppercase):
	return ''.join(random.choice(chars) for _ in range(size))

def get_image_path(instance, filename):
	title = instance.topic.title
	slug = slugify(title)
	return (os.path.join('blog_mcpy' ,'static', slug, filename))

class Topic(models.Model):
	title = models.CharField(max_length=40)
	subtitle = models.CharField(max_length=500, default="Author forgot to put subtitle! LOL")
	text = models.TextField(default="Author forgot to put content! LOL")
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	link = models.CharField(max_length=40, default=link_generator())
	def __str__(self):
		return self.title

class Images(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	def __str__(self):
		return self.image.url
	