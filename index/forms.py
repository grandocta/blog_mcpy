from django.forms import ModelForm, Textarea
from .models import Topic

class TopicForm(ModelForm):
	class Meta:
		model = Topic
		fields = ('title', 'subtitle', 'text')
