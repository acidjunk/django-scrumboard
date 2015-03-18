from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms.models import modelform_factory
from datetimewidget.widgets import DateTimeWidget

from django.core.urlresolvers import reverse_lazy

from scrumtools.apps.wishlist.models import Wish

class WishList(ListView):
    model = Wish
    paginate_by = 10

class WishCreate(CreateView):
    model = Wish
    form_class =  modelform_factory(Wish, widgets={"created_on": DateTimeWidget(usel10n=True, bootstrap_version=3)})
    success_url = reverse_lazy('wishlist:wish_list')


class WishUpdate(UpdateView):
    model = Wish
    form_class =  modelform_factory(Wish, widgets={"created_on": DateTimeWidget(usel10n=True, bootstrap_version=3)})
    success_url = reverse_lazy('wishlist:wish_list')

class WishDelete(DeleteView):
    model = Wish
    success_url = reverse_lazy('wishlist:wish_list')

class WishDetail(DetailView):
    model = Wish
