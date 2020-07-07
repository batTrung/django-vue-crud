from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.utils.timesince import timesince

from .constants import Status
from .managers import BookManager


class Book(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books_created',
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60, unique=True, blank=True)
    status = models.CharField(
        max_length=1,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    description = models.TextField()
    views = models.PositiveIntegerField(default=0)
    photo = models.URLField(blank=True)
    price = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    objects = BookManager()

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Book, self).save(*args, **kwargs)

    @property
    def timeago(self):
        return f'{timesince(self.created)} trước'

