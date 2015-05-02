from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms.models import modelform_factory

from django.core.urlresolvers import reverse_lazy

from scrumtools.apps.wishlist.models import Wish

class WishList(ListView):
    model = Wish
    paginate_by = 10

class WishCreate(CreateView):
    model = Wish
    form_class =  modelform_factory(Wish)
    success_url = reverse_lazy('wishlist:wish-list')
    template_name = 'wishlist/form.html'


class WishUpdate(UpdateView):
    model = Wish
    form_class =  modelform_factory(Wish)
    success_url = reverse_lazy('wishlist:wish-list')
    template_name = 'wishlist/form.html'


class WishDelete(DeleteView):
    model = Wish
    success_url = reverse_lazy('wishlist:wish-list')
    template_name = 'wishlist/confirm_delete.html'


class WishDetail(DetailView):
    model = Wish
