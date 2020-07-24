from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from user.manager import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("Email Address:"),unique=True)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

