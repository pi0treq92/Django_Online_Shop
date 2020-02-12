from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderForm
from basket.basket import Basket
from .tasks import created_order
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

#@staff_member_required
def order_to_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="order_{}.pdf"'.format(order.id)
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    return response


def create_order(request):
    basket = Basket(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for i in basket:
                OrderItem.objects.create(order=order, item=i['item'], price=i['price'], quantity=i['quantity'])
            basket.drop_basket()
            created_order.delay(order.id)
            return render(request, 'orders/order_created.html', {'order': order})
    else:
        form = OrderForm()
    return render(request, 'orders/order_create.html', {'basket': basket, 'form': form})
