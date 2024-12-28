from django.shortcuts import render

# Create your views here.
def func_templ(request):
    return render(request, 'second_task/func_template.html')

def class_templ(request):
    return render(request, 'second_task/class_template.html')
