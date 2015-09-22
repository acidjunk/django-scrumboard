from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.core.urlresolvers import reverse_lazy

from scrumtools.apps.wishlist.models import Wish

class WishList(ListView):
    model = Wish
    fields = ['name', 'description']
    paginate_by = 10

class WishCreate(CreateView):
    model = Wish
    fields = ['name', 'description']
    success_url = reverse_lazy('wishlist:wish-list')
    template_name = 'wishlist/form.html'


class WishUpdate(UpdateView):
    model = Wish
    fields = ['name', 'description']
    success_url = reverse_lazy('wishlist:wish-list')
    template_name = 'wishlist/form.html'


class WishDelete(DeleteView):
    model = Wish
    fields = ['name', 'description']
    success_url = reverse_lazy('wishlist:wish-list')
    template_name = 'wishlist/confirm_delete.html'


class WishDetail(DetailView):
    model = Wish
    #fields = ['name', 'description']
