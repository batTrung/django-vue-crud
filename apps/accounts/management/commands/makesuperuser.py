from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-u', '--username', type=str, default='admin', help='username')
        parser.add_argument('-p', '--password', type=str, default='admin', help='password')

    def handle(self, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        User = get_user_model()
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username, f'{username}@gmail.com', password)
            output = 'Admin user has created:'
            username = '+ username: {:>6}'.format(username)
            password = '+ password: {:>6}'.format(password)
            self.stdout.write(self.style.SUCCESS('\n'.join((output, username, password))))
        else:
            self.stdout.write(self.style.SUCCESS('Admin user already exists.'))
