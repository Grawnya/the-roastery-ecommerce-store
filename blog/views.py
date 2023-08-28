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

    if not request.user.is_superuser:
        pass #error message
        return redirect(reverse('blog'))

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

@login_required
def edit_blog(request, blog_id):

    if not request.user.is_superuser:
        pass #error message
        return redirect(reverse('blog'))

    edit_blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog_form = BlogForm(instance=edit_blog)
        if blog_form.is_valid():
            blog_form.save()
            return redirect('blog')
    else:
        blog_form = BlogForm()

    context = {
        'form': blog_form
    }
    return render(request, 'blog_app/edit_blog.html', context)

@login_required
def delete_blog(request, blog_id):

    if not request.user.is_superuser:
        pass #error message
        return redirect(reverse('blog'))

    delete_blog = get_object_or_404(Blog, id=blog_id)
    delete_blog.delete()
    return redirect(reverse('blog'))
    