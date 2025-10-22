from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.publicados.all().order_by('-criado_em')
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post.publicados, slug=slug)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)


