from django.contrib import admin
from scrumtools.apps.wishlist.models import Wish

class WishAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_on', 'was_published_recently')
    list_filter = ['created_on']
    search_fields = ['name', 'description']
admin.site.register(Wish, WishAdmin)
