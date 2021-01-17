from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('advertisement_master', views.advertisement_master, name='advertisement_master'),
    path('user_info', views.get_client_ip, name='get_client_ip'),
]