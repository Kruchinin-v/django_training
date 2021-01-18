from django.urls import path
from . import views
from .views import About, AdvertisementListView, AdvertisementDetailView

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('about', About.as_view(), name='about'),
    path('user_info', views.get_client_ip, name='get_client_ip'),
    path('advertisements', AdvertisementListView.as_view(), name='advertisements'),
    path('advertisements/<int:pk>', AdvertisementDetailView.as_view(), name='advertisement-detail')
]