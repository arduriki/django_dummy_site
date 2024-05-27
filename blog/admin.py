from django.contrib import admin
from .models import Tag, Author, Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "date", "tags")
    list_display = ("title", "author", "date")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
