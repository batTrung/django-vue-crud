from django.db import models

from .constants import Status


class BookManager(models.Manager):
    def get_queryset(self):
        return super(
            BookManager, self).get_queryset(
            ).select_related(
                'author',
            )
    def published(self):
        query = self.get_queryset()
        return query.filter(status=Status.PUBLISHED)
