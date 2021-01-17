from django.shortcuts import render
from django.http import HttpResponse


def advertisement_list(request, *args, **kwargs):
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика',
    ]
    return render(request, 'advertisement/advertisement_list.html', {'advertisements': advertisements})


def advertisement_master(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_master.html', {})


def get_client_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    return render(request, 'advertisement/user_info.html', {'ip_address': ip})
