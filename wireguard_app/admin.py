from django.contrib import admin
from .models import Peers

class PeersAdmin(admin.ModelAdmin):
    list_display = ['pub_key', 'private_key', 'ip', 'ip_external']

admin.site.register(Peers)

