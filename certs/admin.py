from django.contrib import admin
from .models import QrCod

class QRadmin(admin.ModelAdmin):
    list_display = ['qr_cod', 'valid_date', 'pay_date']

admin.site.register(QrCod)