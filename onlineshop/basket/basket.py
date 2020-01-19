from decimal import Decimal
from django.conf import settings
from shop.models import Item

class Basket(object):
    """
    Class Basket manages basket for shopping. Basket init is unnecessary with object request.
    Current session is keeping by command self.session = request.session
    """
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def add_item(self, item, quantity=1, refresh_quantity=False):
        """
        :param item: Item class object which is added or updating
        :param quantity: optional number of items
        :param refresh_quantity: boolean value indicating if number of items should be update
        :return:  Key item.id (int) and item.price (Decimal) is converting to string for JSON serialization purpose
        """
        item_id = str(item.id)
        if item_id not in self.basket:
            self.basket[item_id] = {'quantity': 0, 'price': str(item.price)}
        if refresh_quantity:
            self.basket[item_id]['quantity'] = quantity
        else:
            self.basket[item_id]['quantity'] += quantity
        self.save()

    def remove_item(self, item):
        """
        Removing item from basket
        :param item:
        :return:
        """
        item_id = str(item.id)
        if item_id in self.basket:
            del self.basket[item_id]
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        """
        Iterating through basket database and taking items from database
        Converting item price to Decimal from dictionary where we put in as string and getting total price
        :return:
        """
        item_ids = self.basket.keys()
        items = Item.objects.filter(id__in=item_ids)
        basket = self.basket.copy()
        for item in items:
            basket[str(item.id)]['item'] = item
        for i in basket.values():
            i['price'] = Decimal(i['price'])
            i['total_price'] = i['price'] * i['quantity']
            yield i

    def __len__(self):
        """
        Counting all elements in the basket
        :return:
        """
        return sum(item['quantity'] for item in self.basket.values())

    def get_total_price(self):
        """
        Calculating total price
        :return: total price
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())

    def drop_basket(self):
        """
        Deleting basket from session
        :return:
        """
        del self.session[settings.BASKET_SESSION_ID]
        self.save()
