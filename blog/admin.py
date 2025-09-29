from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Aqui você pode adicionar configurações para a sua tela de admin,
    # como a exibição de campos, filtros, etc.
    list_display = ('titulo', 'status', 'criado_em')
    list_filter = ('status', 'criado_em')
    search_fields = ('titulo', 'conteudo')