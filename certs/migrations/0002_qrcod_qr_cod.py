# Generated by Django 3.2.9 on 2023-01-09 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('certs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcod',
            name='qr_cod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
