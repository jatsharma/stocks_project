from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Custom user Class.
    """

    username = None
    email = models.EmailField(_("email address"), unique= True)
    name = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email

