from django.contrib import admin
from .models import Category, Item
from parler.admin import TranslatableAdmin


@admin.register(Category)
class CategoriesAdministration(TranslatableAdmin):
    """
    ---------------
    :var
    list_display - show in admin panel properties from the list
    prepopulated_field -  allow to indicate column in which values are automatically input, based on chosen column
                        in this case 'name'
    """
    list_display = ['name', 'slug']
    def get_prepopulated_fields(self, request, obj=None ):
        return {'slug': ('name',)}



@admin.register(Item)
class ItemsAdministration(TranslatableAdmin):
    """
    ---------------
    :var
    list_display - show in admin panel properties from the list
    list_filter - allow to filtering by properties from the list
    list_editable - allow to edit properties from the list
    """
    list_display = ['name', 'price', 'quantity', 'created_at', 'available', 'updated_at', 'slug',]
    list_filter = ['price', 'created_at', 'available',]
    list_editable = ['price', 'available', 'quantity']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}