from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from users.models import CustomUser
import random
import string
from certs.models import QrCod
from django.contrib.auth import get_user_model
import datetime


def random_digit():
    return ''.join(random.choice('1234567890') for _ in range(4)) #random.choice("123456789")


User = get_user_model()


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:

        print('\nCustomUser!!!!!!!!!!!!', sender, instance)
        user = User.objects.get(email=instance)
        qr = QrCod(qr_cod=user)
        qr.qr_hash
        print('user', user)
        qr_serial = random_digit() + ' ' + random_digit() + ' ' + random_digit() + ' ' + random_digit()
        qr_id = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(30))
        dt_now = datetime.datetime.now() + datetime.timedelta(days=int(''.join(random.choice('3456') for _ in range(2)))+30)
        qr.qr_hash = qr_id
        qr.qr_serial = qr_serial
        qr.valid_date = dt_now
        qr.is_valid = True
        qr.save()
