from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views import generic
from django.views.generic import TemplateView
from advertisement.models import Advertisement


def advertisement_list(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisement/advertisements.html', {
        'advertisements': advertisements,
    })


def get_client_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    return render(request, 'advertisement/user_info.html', {'ip_address': ip})


class About(TemplateView):
    template_name = 'advertisement/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Беплатные объявления в вашем городе'
        context['title'] = 'Бесплатные объявления'
        context['description'] = """
        Это типа длинный текст
        Нужно что-то сюда написать
        """
        return context


class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()[:5]


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement