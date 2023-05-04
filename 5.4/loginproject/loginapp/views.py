from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def home(request):
   return render(request, 'home.html')

def signup(request):
   if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       exist_user = User.objects.filter(username=username)

       if exist_user:
          error = "오류다 용용 죽겠지~"
          return render(request, 'signup.html', {"error":error})
       new_user = User.objects.create_user(username=username, password=password)
       auth.login(request, new_user)
       return redirect('blogapp:home')

   return render(request, 'signup.html')

def login(request):
   if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username, password=password)

       if user is not None:
          auth.login(request, user, backend ="django.contrib.auth.backends.ModelBackend")
          return redirect(request.GET.get('next', 'blogapp:home'))
       # {'next': '/new/'} 으로 나타나게 된다.
       error = "틀렸다 이눔아~"
       return render(request, 'login.html',  {"error":error})
   
   return render(request, 'login.html')   