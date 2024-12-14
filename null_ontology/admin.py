from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'created_at', 'updated_at', 'slug']
    list_filter = ['category', 'created_at', 'updated_at']
    search_fields = ['title', 'content', 'slug']
    ordering = ['created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}

admin.site.site_header = 'Null Ontology Administration'
admin.site.site_title = 'Null Ontology Administration'
admin.site.index_title = 'Null Ontology Administration'
