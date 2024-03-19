from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context ={
        'titile': 'TopCase - Главная',
        'content': 'TopCaseOm',
        'list': ['first', 'second'],

    }
    return render(request, 'main/index.html', context)

def about(request):
    context ={
        'titile': 'TopCase - О нас',
        'content': 'О нас',
        'text_on_page': 'Наш магазин, TopCase, Эксперт в подборе аксессуаров к мобильной технике, технике для дома, автомобиля и офиса. Мы предоставляем огромный ассортимент по доступным ценам.TopCase - только оригинальные вещи -лучшее для Вас! :)',
    }

    return render(request, 'main/about.html', context)