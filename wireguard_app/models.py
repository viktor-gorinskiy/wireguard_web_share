from django.db import models
from django.conf import settings
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Peers(models.Model):
    pub_key =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    private_key = models.CharField(max_length=30, blank=True, null=True, help_text="private_key")
    ip = models.CharField(max_length=30, blank=True, null=True, help_text="ip addres")
    ip_external = models.CharField(max_length=30, blank=True, null=True, help_text="ip addres")
    # transfer = 
    # received = 
    # is_valid = models.BooleanField(default=False, help_text="Действителен ли сертификат")
    # valid_date = models.DateField(blank=True, null=True, help_text="Дата окончания действия сертификата")
    # pay_date = models.DateField(blank=True, null=True, help_text="Дата оплаты")

    # qr_serial = models.CharField(max_length=30, blank=True, null=True, help_text="serial QR")
    # qr_hash = models.CharField(max_length=30, blank=True, null=True, help_text="Хэш для QR кода")



    # def email(self):
    #     if self.email:
    #         return getattr(self.email, 'email', None)

    def __str__(self):
        return 'Peers {}'.format(self.qr_cod)