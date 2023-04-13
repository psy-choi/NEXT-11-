from django.shortcuts import render, redirect
from .models import Post, Comment, InnerComment


def home(request):
   posts = Post.objects.all()


   return render(request, 'home.html', {'posts':posts})


def new(request):
   if request.method == "POST":
       title = request.POST['title']
       content = request.POST['content']


       new_post = Post.objects.create(
           title=title,
           content=content)
       return redirect('detail', new_post.pk)
  
   return render(request, 'new.html')

def detail_innercomment(reqeust, post_pk, comment_pk):
   post = Post.objects.get(pk=post_pk)
   comment = Comment.objects.get(pk=comment_pk)
   print(post)
   if reqeust.method == 'POST':
       innercontent = reqeust.POST['innercontent']
       InnerComment.objects.create(
          comment = comment,
          content = innercontent
       )
       return redirect('detail', post_pk)
   return render(reqeust, 'detail.html', {'post':post})


def detail_comment(request, post_pk):
   post = Post.objects.get(pk=post_pk)
   print(post)
   if request.method == 'POST':
       content = request.POST['content']
       Comment.objects.create(
           post = post,
           content = content
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
# Create your views here.

def delete_comment(request, post_pk, comment_pk):
   comment = Comment.objects.get(pk=comment_pk)
   comment.delete()
   return redirect('detail',post_pk)

def delete_innercomment(request, post_pk, innercomment_pk):
   innercomment = InnerComment.objects.get(pk=innercomment_pk)
   innercomment.delete()
   return redirect('detail', post_pk)