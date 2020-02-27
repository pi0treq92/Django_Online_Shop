from django.shortcuts import render, get_object_or_404
from .models import Category, Item
from basket.forms import  AddItemForm

def items_list(request, category_filter=None):
    """

    :param request:
    :param category_filter: demanding filtering value
    :return:
    item_list.html view with the follow dictionary, allows to show and iterating values from the dictionary
    """
    category = None
    categories = Category.objects.all()
    items = Item.objects.filter(available=True) #filtrowanie tylko dostepnych produktów
    if category_filter:
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category, translations__language_code=language,
                                     translations__slug=category_filter)
        items = items.filter(category=category)
    return render(request, 'shop/item/item_list.html', {'category': category, 'categories': categories, 'items': items})

def item_detail(request, id, slug):
    """

    :param request:
    :param id: item id
    :param slug: item slug
    :return:  item_list.html view with the follow dictionary, allows to show and iterating values from the dictionary
    """
    language = request.LANGUAGE_CODE
    item = get_object_or_404(Item, id=id, translations__language_code=language,
                                translations__slug=slug, available=True)
    basket_form = AddItemForm()
    return render(request, 'shop/item/item_detail.html', {'item': item, 'basket_form': basket_form})

