from django.contrib import admin
from .models import OrderItem, Order
import datetime, csv
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['item']

def csv_exporting(modeladmin, request, queryset):
    options = modeladmin.model._meta
    #Browser know to treat as CSV file because of text/csv type
    response = HttpResponse(content_type='text/csv')
    #Content-Disposition header indicates, that Http response contains file
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(options.verbose_name)
    writer = csv.writer(response)
    #Dynamic loading model columns with get_fields() method in _meta options. Many to Many and One to Many excluded.
    fields = [field for field in options.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
        data = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data.append(value)
        writer.writerow(data)
    return response
csv_exporting.short_description = 'Exporting to csv'

def order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(
        reverse('orders:order_to_pdf', args=[obj.id])))
order_pdf.short_description = 'Invoice'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'email', 'street', 'street_number', 'city', 'code', 'paid', 'created',
                    'updated', order_pdf]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [csv_exporting]

admin.site.register(Order, OrderAdmin)
