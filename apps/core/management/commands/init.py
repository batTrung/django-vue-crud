from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        call_command('load_users')
        call_command('makesuperuser')
        call_command('load_books')
