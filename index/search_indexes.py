from django.utils import timezone
from haystack import indexes
from index.models import Topic

class TopicIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)

	def get_model(self):
		return Topic

	def index_queryset(self, using=None):
		return self.get_model().objects.filter(published_date__lte=timezone.now()).order_by('-published_date')