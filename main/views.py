from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from goods.models import Categories




class IndexView(TemplateView):
    template_name = 'main/index.html'


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'TopCase - Главная'
    context['content'] = "TopCaseOm"
    return context



class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'TopCase - О нас'
        context['content'] = "О нас"
        context['text_on_page'] = 'Наш магазин, TopCase, Эксперт в подборе аксессуаров к мобильной технике, технике для дома, автомобиля и офиса. Мы предоставляем огромный ассортимент по доступным ценам.TopCase - только оригинальные вещи -лучшее для Вас!:)',