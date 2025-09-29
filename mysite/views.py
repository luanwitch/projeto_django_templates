from django.shortcuts import render
from .models import Post # type: ignore

def index(request):
    posts = Post.objects.filter(status="published").order_by("-criado_em")
    return render(request, "blog/index.html", {"posts": posts})
