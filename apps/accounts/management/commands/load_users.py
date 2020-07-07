from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-u', '--user', type=int, default=100, help='Number users')

    def handle(self, *args, **kwargs):
        num_u = kwargs['user']

        self.stdout.write("Cleaning database...")
        User.objects.all().delete()

        self.stdout.write(self.style.HTTP_NOT_MODIFIED(f"Creating users..."))

        users = [
            User(
                username=f'user_{i}',
                email=f'user_{i}@gmail.com',
                password=make_password('matkhau123'),
            ) for i in range(num_u)
        ]
        User.objects.bulk_create(users)

        self.stdout.write(
            self.style.SUCCESS(f'SUCCESSFULLY CREATED: { num_u } users')
        )
