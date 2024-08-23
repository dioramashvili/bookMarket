from django.contrib import admin

from market.models import Book


class MarketAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_name', 'price')
    search_fields = ('name', 'author_name')
    list_per_page = 3


admin.site.register(Book, MarketAdmin)
