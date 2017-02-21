from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Topic, link_generator
from .forms import TopicForm
from django.contrib.auth.decorators import login_required

def index(request):
	recent = Topic.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
	random = Topic.objects.filter(published_date__lte=timezone.now()).order_by('?')[:5]
	zipped = zip(recent,random)
	return render(request, 'index.html', {'recent': recent, 'random': random, 'zipped':zipped,})

def details(request, plink):
	topic = get_object_or_404(Topic, link=plink)
	return render(request, 'details.html', {'topic':topic, })

@login_required
def post_new(request):
	if request.method == "POST":
		form = TopicForm(request.POST)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.link = link_generator()
			topic.save()
			return redirect('details', plink=topic.link)
	else:
		form = TopicForm()
	return render(request, 'edit.html', {'form':form,})

@login_required
def post_edit(request, plink):
	topic = get_object_or_404(Topic, link=plink)
	if request.method == "POST":
		form = TopicForm(request.POST, instance=topic)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.save()
			return redirect('details', plink=topic.link)
	else:
		form = TopicForm(instance=topic)
	return render(request, 'edit.html', {'form':form, })

def archive(request):
	recent = Topic.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	drafts = Topic.objects.filter(published_date=None).order_by('-created_date')
	return render(request, 'archive.html', {'recent':recent, 'drafts':drafts, })

def post_publish(request, plink):
	topic = get_object_or_404(Topic, link=plink)
	topic.published_date=timezone.now()
	topic.save()
	return redirect('details', plink=topic.link)