from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    forma = AutoForm()
    base = Auto.objects.all()
    data = {'forma': forma, 'base': base}
    return render(request, 'index.html', context=data)
    pass


def write(request):
    if request.POST:
        auto = Auto()
        auto.auto_model = request.POST.get('auto_model')
        auto.auto_country = request.POST.get('auto_country')
        auto.auto_year = request.POST.get('auto_year')
        auto.auto_number = request.POST.get('auto_number')
        auto.save()
        return redirect('home')
        pass


def delete(request, ids):
    ids = int(ids)
    auto = Auto.objects.get(id=ids)
    auto.delete()
    return redirect('home')
    pass
