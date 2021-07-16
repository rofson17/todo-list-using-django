from typing import ItemsView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem


# Create your views here.


def index(request):
    itmes = TodoItem.objects.all()
    return render(request, 'index.html', {'all_items': itmes})


def add(request):
    if request.method == "POST":
        item = request.POST['content']
        s = TodoItem(content=item)
        s.save()
        return HttpResponseRedirect('/todo/')
    return HttpResponse('please add the any item to the to do list')


def deleteItem(request, id):
    items = TodoItem.objects.get(id=id)
    items.delete()

    return HttpResponseRedirect('/todo/')


def editItem(request, id):
    item = TodoItem.objects.get(id=id)
    if request.method == "GET":
        return render(request, 'edit.html', {'content': item.content, 'id': id})

    else:
        i = request.POST['content']
        item.content = i
        item.save()
        return HttpResponseRedirect('/todo/')
