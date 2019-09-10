from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *

# Create your views here.

def index(request):
    if request.method == 'GET':
        todo_items = TodoItem.objects.all()
        context = {
            'todos': todo_items
        }
        return render(request, 'todoapp/index.html', context)

    if request.method == "POST":
        todo_item = TodoItem()
        todo_item.title = request.POST['title']
        todo_item.status = False
        todo_item.save()
        return HttpResponseRedirect(reverse('todoapp:index'))
