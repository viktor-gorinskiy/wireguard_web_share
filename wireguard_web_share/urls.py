from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', include('users.urls')),
    # path('certs/', include('certs.urls')),
    path('account/', include('users.urls')),
    path('accounts/', include('users.urls')),
    ]