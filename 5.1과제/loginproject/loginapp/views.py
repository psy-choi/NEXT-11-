from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment


# Create your views here.


def home(request):
   posts = Post.objects.all()

   return render(request, 'home.html', {'posts':posts})

def logout(request):
   auth.logout(request)
   return redirect('home')

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
       return redirect('home')

   return render(request, 'signup.html')


def login(request):
   if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username, password=password)

       if user is not None:
          auth.login(request, user, backend ="django.contrib.auth.backends.ModelBackend")
          return redirect(request.GET.get('next', '/'))
       # {'next': '/new/'} 으로 나타나게 된다.
       error = "틀렸다 이눔아~"
       return render(request, 'login.html',  {"error":error})
   
   return render(request, 'login.html')   


@login_required(login_url="login/")
def new(request):
   if request.method == "POST":
       title = request.POST['title']
       content = request.POST['content']


       new_post = Post.objects.create(
           title=title,
           content=content,
           author = request.user)
       return redirect('detail', new_post.pk)
  
   return render(request, 'new.html')


@login_required(login_url="login/")
def detail(request, post_pk):
   post = Post.objects.get(pk=post_pk)
   
   if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            post=post,
            content=content,
            author = request.user
        )
        return redirect('detail', post_pk)

   return render(request, 'detail.html', {'post':post})


def edit(request, post_pk):
   post = Post.objects.get(pk=post_pk)


   if request.method == 'POST':
       title = request.POST['title']
       content = request.POST['content']
       Post.objects.filter(pk=post_pk).update(
           title=title,
           content=content
       )
       return redirect('detail', post_pk)


   return render(request, 'edit.html', {'post':post})




def delete(request, post_pk):
   post = Post.objects.get(pk=post_pk)
   post.delete()
   return redirect('home')


def delete_comment(request, post_pk, comment_pk):
   comment = Comment.objects.get(pk=comment_pk)
   comment.delete()
   return redirect('detail', post_pk)