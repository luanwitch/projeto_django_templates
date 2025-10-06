from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'criado_em', 'author')
    list_filter = ('status', 'criado_em', 'author')
    search_fields = ('titulo', 'conteudo')
