from .models import Item
from django.conf import settings
import redis


redis_database = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

class Recommendation(object):
    def get_item_id(self, id):
        return 'item:{}:bought_with'.format(id)

    def item_bought(self, items):
        items = [i.id for i in items]
        for id in items:
            for recommendation in items:
                if id != recommendation:
                    redis_database.zincrby(self.get_item_id(id), recommendation, amount=1)


    def suggestion(self, items, max=5):
        item_ids = [i.id for i in items]
        if len(items) == 1:
            # just one item
            suggestions = redis_database.zrange(self.get_item_id(item_ids[0]), 0, -1, desc=True)[:max]
        else:
            # Basic key generating
            flat = ''.join([str(id) for id in item_ids])
            temp_key = 'temp_{}'.format(flat)
            # Suming all product keys
            # Putting sorted results collection in temporary key
            keys = [self.get_item_id(id) for id in item_ids]
            redis_database.zunionstore(temp_key, keys)
            # Removing item identifiers for recommendation
            redis_database.zrem(temp_key, *item_ids)
            # Downloading product identifiers in descending order according their punctation
            suggestions = redis_database.zrange(self.get_item_id(item_ids[0]), 0, -1, desc=True)[:max]
            # Deleting basic key
            redis_database.delete(temp_key)
        suggested_id = [int(id) for id in suggestions]
        suggested_items = list(Item.objects.filter(id__in=suggested_id))
        suggested_items.sort(key=lambda x: suggested_id.index(x.id))
        return suggested_items

    def remove_purchase(self):
        for id in Item.objects.values_list('id', flat=True):
            redis_database.delete(self.get_item_id(id))