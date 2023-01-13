from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=60, blank=True, null=True, help_text="Фамилия")
    last_name = models.CharField(max_length=60, blank=True, null=True, help_text="Имя")
    # patronymic = models.CharField(max_length=60, blank=True, null=True, help_text="Отчество")

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    date_of_birth = models.DateField(blank=True, null=True, help_text="Дата рождения")
    # passport_serial = models.PositiveIntegerField(blank=True, null=True, help_text="Серия")
    # passport_number = models.PositiveIntegerField(blank=True, null=True, help_text="Номер")


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
