from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def created_order(order_id):
    """
    Method sends notification as email after order object is created.
    :param order_id:
    :return:

    How to run asynchronus task:

    In 1st shell:
    celery -A onlineshop flower

    In 2nd shell:
    onlineshop>celery -A onlineshop worker -l info -P gevent

    In 3nd shell:
    python manage.py runserver

    To show tasks in flower:
    http://localhost:5555/
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order no. {}'.format(order.id)
    message = 'Hello, {}!\n\n\nYou placed the order\nYour order no. {}'.format(order.name, order.id)
    mail = send_mail(subject, message, 'admin@wp.pl', [order.email])
    return mail