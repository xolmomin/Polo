from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import Product, Category, User, Discount, Gender, Color


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'Quantity']
    # fields = ['title', 'price', 'description']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'id', 'slug', 'product_count']
    fields = ['image', 'name']

    def product_count(self, obj):
        return obj.product_set.count()


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    search_fields = ['percent']
    list_display = ['id', 'slug', 'percent']
    fields = ['percent']

    def product_count(self, obj):
        return obj.product_set.count()


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    search_fields = ['sex']
    list_display = ['id', 'slug', 'sex']
    fields = ['sex']

    def product_count(self, obj):
        return obj.product_set.count()


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    search_fields = ['colour']
    list_display = ['id', 'slug', 'colour']
    fields = ['colour']

    def product_count(self, obj):
        return obj.product_set.count()


admin.site.register(User, UserAdmin)
