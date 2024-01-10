from django.contrib import admin
from .models import Collections, Market

class ShowCollecctions(admin.ModelAdmin):
    list_display =('image', 'name', 'category', 'items_in_collection')
admin.site.register(Collections, ShowCollecctions)

class ShowMarket(admin.ModelAdmin):
    list_display = ('image', 'name', 'author_name', 'author_link', 'ends_in', 'current_bid', 'current_price')
admin.site.register(Market, ShowMarket)

# Register your models here.
