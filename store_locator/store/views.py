from django.views.generic import ListView
from django.utils import timezone

from store.models import Store
from product.models import Product

class IndexListView(ListView):
    model = Store

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class StoreDetailListView(ListView):
	model = Product
	template_name = "store/store_detail.html"
	context_object_name = 'products'

	def get_context_data(self, **kwargs):
	    context = super(StoreDetailListView, self).get_context_data(**kwargs)
	    context['now'] = timezone.now()
	    store_name = Store.objects.get(id = self.kwargs['pk'])
	    context['store_name'] = store_name
	    return context

	def get_queryset(self):
		pk = self.kwargs['pk']
		return Product.objects.filter(available_in=pk)