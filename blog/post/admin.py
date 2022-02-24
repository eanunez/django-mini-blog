from django.contrib import admin
from .models import Post, Comment, User

from django.contrib.auth.models import Group


# admin.register() decorator
@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    pass


admin.site.register(User)

# admin.site.register(Post)
admin.site.register(Comment)

# admin.site.unregister(Group)

admin.site.site_header = "Blog Admin"
