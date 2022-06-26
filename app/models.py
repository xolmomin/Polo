from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import integer_validator
from django.db.models import (Model,
                              DateTimeField,
                              CharField,
                              Model,
                              ImageField, EmailField, IntegerField, ForeignKey, SET_NULL)
from django.forms import SlugField, FloatField
from django.utils.text import slugify


class BaseModel(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(BaseModel):
    pass


class Product(BaseModel):
    title = CharField(max_length=255)
    category = ForeignKey('app.Category', SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title


class Category(Model):
    parent = ForeignKey('app.Category', SET_NULL, blank=True, null=True)
    image = ImageField(upload_to='category/')
    name = CharField(max_length=255)
    # slug = SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.name)
            while Category.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-1'

        super().save(force_insert, force_update, using, update_fields)
