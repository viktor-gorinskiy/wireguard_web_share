# Create your models here.
from django.db import models
from django.conf import settings
from django.db import models
from django.conf import settings
# from phone_field import PhoneField
# from django.contrib.auth.models import User
from django.urls import reverse

from django.dispatch import receiver
from django.db.models.signals import post_save


class QrCod(models.Model):
    qr_cod = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    is_valid = models.BooleanField(default=False, help_text="Действителен ли сертификат")
    valid_date = models.DateField(blank=True, null=True, help_text="Дата окончания действия сертификата")
    pay_date = models.DateField(blank=True, null=True, help_text="Дата оплаты")

    qr_serial = models.CharField(max_length=30, blank=True, null=True, help_text="serial QR")
    qr_hash = models.CharField(max_length=30, blank=True, null=True, help_text="Хэш для QR кода")



    def email(self):
        if self.email:
            return getattr(self.email, 'email', None)       # attempt to access username

    def __str__(self):
        return 'Qr for user {}'.format(self.qr_cod)
