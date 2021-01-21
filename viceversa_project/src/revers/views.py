from django.shortcuts import render


def revers(request):
    return render(request, 'revers/index.html')
