from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from app.models import Product, User, Category, Blog, BlogCategory, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = ['id', 'title', 'price', 'quantity']
    # fields = ['title', 'price', 'description']
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


class CustomMPTTModelAdmin(DraggableMPTTAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20


admin.site.register(Category, CustomMPTTModelAdmin)
admin.site.register(BlogCategory, CustomMPTTModelAdmin)
