from django.contrib.auth.models import (  # noqa
    AbstractUser, UserManager as AbstractUserManager
)


class CustomUserManager(AbstractUserManager):

    def get_queryset(self):
        return super(
            CustomUserManager, self).get_queryset(
            )
