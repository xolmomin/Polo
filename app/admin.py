from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from app.models import Product, User, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = ['id', 'title', 'price', 'quantity']
    # fields = ['title', 'price', 'description']
    pass


class CustomMPTTModelAdmin(DraggableMPTTAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20


admin.site.register(Category, CustomMPTTModelAdmin)
