import random

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from apps.common.helpers import get_random_obj

from apps.bookstore.constants import Status
from apps.bookstore.models import Book

User = get_user_model()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-b', '--book', type=int, default=100, help='Number books')

    def handle(self, *args, **kwargs):
        num_b = kwargs['book']

        self.stdout.write("Cleaning database...")
        Book.objects.all().delete()

        self.stdout.write(self.style.HTTP_NOT_MODIFIED(f"Creating Books..."))
        books = [
            Book(
                author=get_random_obj(User),
                name=f'Book name {i}',
                slug=get_random_string(20),
                status=random.choice(Status.choices)[0],
                description='Descriton book',
                price=random.randint(50, 1000)*1000,
                photo='https://images-na.ssl-images-amazon.com/images/I/51l5XzLln+L._SY344_BO1,204,203,200_.jpg',
            ) for i in range(num_b)
        ]
        Book.objects.bulk_create(books)

        self.stdout.write(
            self.style.SUCCESS(f'SUCCESSFULLY CREATED: {num_b} books')
        )
