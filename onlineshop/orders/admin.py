from django.contrib import admin
from .models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['item']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'email', 'street', 'street_number', 'city', 'code', 'paid', 'created',
                    'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
