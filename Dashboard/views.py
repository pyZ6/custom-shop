from django.shortcuts import render

from .forms import DashForm

def validation_form(request):
    context = {}
    form = DashForm(request.POST)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'Dashboard/validation_form.html', context)