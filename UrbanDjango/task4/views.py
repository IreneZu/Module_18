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
    return render(request, 'fourth_task/platform.html', context)

class buildings(TemplateView):
    template_name = 'fourth_task/buildings.html'
    title = 'MKD'
    header = 'Список МКД'
    cont_buildings = ['Задонский пр., д.14, к.2', 'Задонский пр., д.16, к.1', 'Задонский пр., д.16, к.2']
    extra_context = {
        'title' : title,
        'header' : header,
        'buildings': cont_buildings,
    }

class management_org(TemplateView):
    template_name = 'fourth_task/management_org.html'
    title = 'UO'
    header = 'Управляющая организация'
    extra_context = {
        'title' : title,
        'header' : header,
    }
