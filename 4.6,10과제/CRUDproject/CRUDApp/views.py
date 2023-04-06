from django.shortcuts import render, redirect
from .models import Todo
from django.db.models import F
from datetime import date

# Create your views here.



def home(request):
    todoes = Todo.objects.all().order_by(F('deadline').asc(nulls_last=True))
    today = date.today()
    d_days = []
    for todo in todoes:
        d_day = todo.deadline - today
        d_days.append(d_day.days)
    todos = zip(todoes, d_days)
    return render(request,	'home.html', {'todos': todos})

def new(request):
    if request.method == 'POST':
        new_todo = Todo.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline']
        )
        return redirect('detail', new_todo.pk)
    return render(request,	'new.html')


def detail(request,	todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    today = date.today()
    d_day = (todo.deadline - today).days
    return render(request,	'detail.html',	{'todo': todo, 'd_day': d_day})

def update(request,	todo_pk):
    todo = Todo.objects.get(pk=todo_pk)

    if request.method == 'POST':
        updated_todo = Todo.objects.filter(pk=todo_pk).update(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail', todo_pk)
    
    return render(request,	'update.html',	{'todo': todo})


def delete(request,	todo_pk):
    todo= Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('home')