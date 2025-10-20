from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'criado_em') 
    list_filter = ('status', 'criado_em')             
    search_fields = ('titulo', 'conteudo')
    prepopulated_fields = {'slug': ('titulo',)}
