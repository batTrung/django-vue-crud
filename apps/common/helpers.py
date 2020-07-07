import random

from django.db.models import Max


def get_random_obj(cls):
    max_id = cls.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        category = cls.objects.filter(pk=pk).first()
        if category:
            return category
