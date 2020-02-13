from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

app_name = 'basket'

urlpatterns = [
    path('', views.basket_detail, name='basket_detail'),
    path(_('add')+'/<int:item_id>/', views.basket_add, name='basket_add'),
    path(_('remove')+'/<int:item_id>/', views.basket_remove, name='basket_remove'),
]