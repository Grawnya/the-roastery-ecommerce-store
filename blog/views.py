from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def view_blog(request):
    entries = BlogEntry.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/blog.html', context)

@login_required
def create_blog(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            blog_form.save()
            return redirect('blog')
    else:
        blog_form = BlogForm()

    context = {
        'form': blog_form
    }
    return render(request, 'blog_app/new_blog.html', context)