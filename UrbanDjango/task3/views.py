from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def platform(request):
    title = 'Main'
    header = 'Главная страница'
    context = {
        'title' : title,
        'header' : header,
    }
    return render(request, 'third_task/platform.html', context)

class buildings(TemplateView):
    template_name = 'third_task/buildings.html'
    title = 'MKD'
    header = 'Список МКД'
    extra_context = {
        'title' : title,
        'header' : header,
    }

class management_org(TemplateView):
    template_name = 'third_task/management_org.html'
    title = 'UO'
    header = 'Управляющая организация'
    extra_context = {
        'title' : title,
        'header' : header,
    }
