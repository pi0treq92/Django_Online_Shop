from django.shortcuts import render
from .models import OrderItem
from .forms import OrderForm
from basket.basket import Basket

def create_order(request):
    basket = Basket(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for i in basket:
                OrderItem.objects.create(order=order, item=i['item'], price=i['price'], quantity=i['quantity'])
            basket.drop_basket()
            return render(request, 'orders/order_created.html', {'order': order})
    else:
        form = OrderForm()
    return render(request, 'orders/order_create.html', {'basket': basket, 'form': form})
