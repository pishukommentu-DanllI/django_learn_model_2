from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .forms import *
from .models import Text
from django.urls import reverse


def index(request):
    return render(request, 'app/index.html', {'pages': Text.objects.all()})


def form(request):
    if request.method == 'POST':
        form = One(request.POST)
        if form.is_valid():
            Text.objects.create(title=form.cleaned_data['Title'], content=form.cleaned_data['TextArea'], img_href=form.cleaned_data['Url'], CheckBox=form.cleaned_data['CheckBox'], Selection=form.cleaned_data['Selection'])
            return HttpResponseRedirect(reverse('home'))
    else:
        form = One()
    return render(request, 'app/form.html', {'form': form})


def edit(request, id):
    if request.method == 'POST':
        try:
            cart = Text.objects.get(id=id)
        except:
            return HttpResponseNotFound('<h2>Person not found</h2>')
        form = One(request.POST)
        if form.is_valid():
            cart.title = form.cleaned_data['Title']
            cart.img_href = form.cleaned_data['Url']
            cart.content = form.cleaned_data['TextArea']
            cart.CheckBox = form.cleaned_data['CheckBox']
            cart.Selection = form.cleaned_data['Selection']
            cart.save()
            return HttpResponseRedirect(reverse('home'))

    else:
        form = One()

    return render(request, 'app/edit.html', {'form': form})


def delete(request, id):
    try:
        cart = Text.objects.get(id=id)
    except:
        return HttpResponseNotFound('<h2>Person not found</h2>')
    cart.delete()
    return HttpResponseRedirect(reverse('home'))
