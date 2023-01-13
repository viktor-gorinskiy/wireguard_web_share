from django.urls import path
from . import views
from django.conf.urls import include, url

#covid-cert/status/9c415f17-

urlpatterns = [
    # url(r'^user_create/$', views.user_create, name='user_create'),
    # url(r'^status/(?P<pk>[\w]+)$', views.ProfileDetailView.as_view(), name='status_qr'),
    url(r'^(?P<qr_id>[\w]+)$', views.ProfileDetailView.as_view(), name='status_qr'),
    # url(r'^qr_gen/$', views.qr_gen, name='qr_gen'),

    # url(r'status_/*', views.status_qr, name='status_qr')
    ]