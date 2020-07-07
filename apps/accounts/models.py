from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    objects = CustomUserManager()
