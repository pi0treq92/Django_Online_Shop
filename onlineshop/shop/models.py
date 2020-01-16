from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    Klasa Category

    --------------
    :parameter
    :name - name of category
    :slug - made from name, has to be unique

    --------------
    :return
    object class Category

    --------------
    :keyword
    category, categories
    """

    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = ('category')
        verbose_name_plural = ('categories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """

        :return: methods is using for getting url address of given object, using url address patterns defined in urls.py
        """
        return reverse('shop:item_list_filter_by_category', args=[self.slug])


class Item(models.Model):
    """
        Class Item

        --------------
        :parameter
        name - name of category
        slug - made from name, has to be unique
        image - may be blank
        info - information about item


        --------------
        :return
        object class Category

        --------------
        :keyword
        item, items
        """
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    image = models.ImageField(upload_to='items/%Y/%m', blank=True)
    info = models.TextField(max_length=300, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('price', 'name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        """
        :return:
        string of name
        """
        return self.name

    def get_absolute_url(self):
        """
        :return:
        string of item id and slug
        """
        return reverse('shop:item_detail', args=[self.id, self.slug])