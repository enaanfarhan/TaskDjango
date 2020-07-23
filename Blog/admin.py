from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(blog, PostAdmin)
admin.site.register(Author)
