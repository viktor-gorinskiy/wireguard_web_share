from django.urls import path
from . import views
from django.conf.urls import include, url
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    # path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name='you_html.html'),name = 'login'),
    # path('logout/', auth_views.LogoutView.as_view, name='logout'),
    url('', include('django.contrib.auth.urls')),
    # path('', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    # url(r'^home/$', views.edit, name='edit'),
    url(r'^registration/$', views.register, name='registration'),
    url(r'^edit/$', views.edit, name='edit'),
    ]
