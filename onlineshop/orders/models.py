from django.db import models
from shop.models import Item
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    """
    Order model contain columns which keep information about customer and the field paid which tell if order was paid
    or not
    """
    name = models.CharField(_('name'), max_length=30)
    surname = models.CharField(_('surname'), max_length=50)
    email = models.EmailField(_('email'),)
    street = models.CharField(_('street'), max_length=100)
    street_number = models.PositiveIntegerField(_('street_number'), )
    city = models.CharField(_('city'), max_length=30)
    code = models.CharField(_('code'), max_length=6)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)
    paid = models.BooleanField(_('paid'), default=False)
    nip = models.CharField(max_length=13, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_price_of_order(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """
    OrderItem model keep information about item from the order
    """
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        """
        :return: total cost of order item
        """
        return self.price * self.quantity
