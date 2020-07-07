from django.db import models


class Status(models.TextChoices):
    DRAFT = 'D', 'Draft'
    PUBLISHED = 'P', 'Published'
