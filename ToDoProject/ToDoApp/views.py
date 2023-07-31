from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ToDoItem
from django.http import HttpResponseRedirect 

@login_required
def HomePage(request):
    user_tasks = ToDoItem.objects.filter(user=request.user)
    if user_tasks.exists():
        return render(request, 'todolist.html', {'all_items': user_tasks})
    else:
        return render(request, 'todolist.html', {})

def Register(request):
    if(request.method == 'POST'):
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        new_user = User.objects.create_user(user_name, email, password)
        new_user.save()
        return redirect('login-page')

    return render(request, 'register.html', {})

def Login(request):
    if(request.method == 'POST'):
        user_name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse('Error: No username or password')

    return render(request, 'login.html', {})    

def logout_view(request):
    logout(request)
    return redirect('login-page')

@login_required
def to_do_app_view(request):
    all_todo_items = ToDoItem.objects.filter(user=request.user)
    return render(request, 'todolist.html',
    {'all_items':all_todo_items}) 

@login_required
def add_to_do_view(request):
    x = request.POST['content']
    new_item = ToDoItem(user=request.user, content = x)
    new_item.save()
    return HttpResponseRedirect('/list/') 

@login_required
def delete_item_view(request, i):
    deleted_item = ToDoItem.objects.get(id = i, user = request.user)
    deleted_item.delete()
    return HttpResponseRedirect('/list/')     