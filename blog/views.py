from django.shortcuts import get_object_or_404, render
from .models import Post

def index(request):
    posts = Post.objects.filter(status='published').order_by('-criado_em')
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})