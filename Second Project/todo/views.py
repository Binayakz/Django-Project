from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def index(request):
    tasks = Todo.objects.all()
    form = TodoForm()

    if request.method == 'POST':

        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'todo/index.html', {'tasks': tasks, 'form': form})


def updateItem(request, pk):
    todo = Todo.objects.get(id=pk)
    updateForm = TodoForm(instance=todo)
    if request.method == 'POST':
        updateForm = TodoForm(request.POST, instance=todo)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('index')
    return render(request, 'todo/update_todo.html', {'todo': todo, 'updateform': updateForm})


def deleteItem(request, pk):
    task = Todo.objects.get(id=pk)
    task.delete()
    return redirect('index')

