from django.contrib import admin
from .models import Post

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=('title',)
    list_filter=("title","disc",)

admin.site.register(Post)