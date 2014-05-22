from django.views.generic.list import ListView
from django.utils import timezone

from store.models import Store

class IndexListView(ListView):
    model = Store

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
