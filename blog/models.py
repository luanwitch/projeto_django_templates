from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    status = models.CharField(max_length=10, default='draft')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default= 1)

    def __str__(self):
        return self.titulo
