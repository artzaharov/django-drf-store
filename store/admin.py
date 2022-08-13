from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
	list_display = ('id', 'slug', 'warehouse', 'status')
	list_display_links = ('id', 'slug')
	search_fields = ('slug',)


class WarehouseAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'url', 'token')
	list_display_links = ('id', 'title')


admin.site.register(Status)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Order, OrderAdmin)
