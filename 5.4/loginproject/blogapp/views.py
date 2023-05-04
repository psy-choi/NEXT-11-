from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment


# Create your views here.


def home(request):
   posts = Post.objects.all()

   return render(request, 'blogapp/home.html', {'posts':posts})


def logout(request):
   auth.logout(request)
   return redirect('home')



@login_required(login_url="login/")
def new(request):
   if request.method == "POST":
       title = request.POST['title']
       content = request.POST['content']


       new_post = Post.objects.create(
           title=title,
           content=content,
           author = request.user)
       return redirect('blogapp:detail', new_post.pk)
  
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
        return redirect('blogapp:detail', post_pk)

   return render(request, 'detail.html', {'post':post})


@login_required(login_url="login/")
def edit(request, post_pk):
   post = Post.objects.get(pk=post_pk)


   if request.method == 'POST':
       title = request.POST['title']
       content = request.POST['content']
       Post.objects.filter(pk=post_pk).update(
           title=title,
           content=content
       )
       return redirect('blogapp:detail', post_pk)


   return render(request, 'edit.html', {'post':post})



@login_required(login_url="login/")
def delete(request, post_pk):
   post = Post.objects.get(pk=post_pk)
   post.delete()
   return redirect('blogapp:home')

@login_required(login_url="login/")
def delete_comment(request, post_pk, comment_pk):
   comment = Comment.objects.get(pk=comment_pk)
   comment.delete()
   return redirect('blogapp:detail', post_pk)