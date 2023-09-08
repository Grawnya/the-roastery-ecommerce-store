from django import forms
from .models import *


class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ['heading', 'blog_body']