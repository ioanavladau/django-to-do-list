from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse

from .models import *


@login_required
def index(request):
    if request.method == 'GET':
        # first user from TodoItem, comparing it to request.user
        todo_items = TodoItem.objects.filter(user=request.user) 
        context = {
            'todos': todo_items
        }
        return render(request, 'todoapp/index.html', context)

    if request.method == "POST":
        todo_item = TodoItem()
        todo_item.title = request.POST['title']
        todo_item.description = request.POST['description']
        todo_item.status = False
        todo_item.user = request.user
        todo_item.save()
        return HttpResponseRedirect(reverse('todoapp:index'))

    return HttpResponseBadRequest()

@login_required
def details(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)

    if request.method == 'GET':
        context = {
            'todo': todo
        }
        return render(request, 'todoapp/details.html', context)

    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        status = request.POST.getlist('status')
        if len(status) > 0:
            todo.status = True
        else:
            todo.status = False
        todo.save()
        return HttpResponseRedirect(reverse('todoapp:index'))

    return HttpResponseBadRequest()



