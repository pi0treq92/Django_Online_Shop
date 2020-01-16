from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.items_list, name='item_list'),
    path('<slug:category_filter>/', views.items_list, name='item_list_filter_by_category'),
    path('<int:id>/<slug:slug>/', views.item_detail, name='item_detail'),
]