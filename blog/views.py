from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def view_blog(request):
    blogs = Blog.objects.all()
    timeline = OurStory.objects.all()
    context = {
        'blogs': blogs,
        'timeline': timeline
    }
    return render(request, 'blog/blog.html', context)

@login_required
def create_blog(request):

    if not request.user.is_superuser:
        messages.error(request, 'An error occurred. Please try again later.')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            blog_form.save()
            messages.success(request, 'Blog post created successfully.')
            return redirect('blog')
    else:
        blog_form = BlogForm()

    context = {
        'form': blog_form
    }
    return render(request, 'blog/new_blog.html', context)

@login_required
def edit_blog(request, blog_id):

    if not request.user.is_superuser:
        messages.error(request, 'An error occurred. Please try again later.')
        return redirect(reverse('blog'))

    edit_blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, instance=edit_blog)
        if blog_form.is_valid():
            blog_form.save()
            messages.success(request, 'Blog post edited successfully.')
            return redirect('blog')
    else:
        blog_form = BlogForm(instance=edit_blog)

    context = {
        'form': blog_form,
        'blog': edit_blog
    }
    return render(request, 'blog/edit_blog.html', context)

@login_required
def delete_blog(request, blog_id):

    if not request.user.is_superuser:
        messages.error(request, 'An error occurred. Please try again later.')
        return redirect(reverse('blog'))

    delete_blog = get_object_or_404(Blog, id=blog_id)
    delete_blog.delete()
    messages.success(request, 'Blog post deleted successfully.')
    return redirect(reverse('blog'))
    