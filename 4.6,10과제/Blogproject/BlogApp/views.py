from django.shortcuts import render, redirect
from datetime import datetime
from .models import Blog, Category


# Create your views here.


def new(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        new_blog = Blog.objects.create(
            title=request.POST['title'],
            content = request.POST['content'],
            category = Category.objects.get(id=request.POST['category']),
            created_at= datetime.now()
        )
        return redirect("list")


    return render(request, "new.html", {'categories': categories})


def list(request):
    categories = Category.objects.all()
    return render(request, "list.html", {"categories":categories})


def list_category(request, category_id):
    category = Category.objects.get(id=category_id)
    blogs = Blog.objects.filter(category__id = category_id)
    return render(request, "list_category.html", {"category":category, "blogs":blogs})



def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, "detail.html", {"blog":blog})