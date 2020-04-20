from django.shortcuts import render, get_object_or_404
from .models import BlogProject


def blog_home(request):
    blog_model = BlogProject.objects.order_by('-date')
    return render(request, 'blog/blog_home.html', {'blogs': blog_model})


def details(request, blog_id):
    blog = get_object_or_404(BlogProject, pk=blog_id)
    return render(request, 'blog/details.html', {'blog': blog})