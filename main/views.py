from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context ={
        'titile': 'Home',
        'content': 'Главная страница магазина - TopCaseOm',
        'list': ['first', 'second'],
        'dict': {'first': 1, 'second': 2},
        'is_authenticated': True
    }
    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    return HttpResponse('About page')
