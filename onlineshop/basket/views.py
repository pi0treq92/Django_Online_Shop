from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Item
from .forms import AddItemForm
from .basket import Basket

@require_POST
def basket_add(request, item_id):
    """
    Decorator let only on POST demand, because view will change data.
    :param request:
    :param item_id:
    :return: redirect to basket_detail
    """
    basket = Basket(request)
    item = get_object_or_404(Item, id=item_id)
    form = AddItemForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add_item(item=item, quantity=cd['quantity'], refresh_quantity=cd['refresh'])
    return redirect('basket:basket_detail')

def basket_remove(request, item_id):
    basket = Basket(request)
    item = get_object_or_404(Item, id=item_id)
    basket.remove_item(item)
    return redirect('basket:basket_detail')

def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/basket_detail.html', {'basket': basket})
