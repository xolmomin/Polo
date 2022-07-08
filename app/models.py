from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import integer_validator
from django.db.models import (
    FloatField, CharField, IntegerField, Model, ImageField, CASCADE, ForeignKey, EmailField, DateTimeField, SlugField,
    SET_NULL, TextField)
from django.utils.text import slugify
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class BaseModel(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User should have phone number ! ')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_comment(self, email, **extra_fields):
        if not email:
            raise ValueError('User should be tested ')
        comment = self.model(email=email, **extra_fields)
        comment.save(using=self._db)
        return comment

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = EmailField(unique=True)
    phone_number = CharField(max_length=25, validators=[integer_validator])
    address = CharField(max_length=255, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Product(BaseModel):
    title = CharField(max_length=255)
    category = TreeForeignKey('app.Category', SET_NULL, blank=True, null=True)
    image = ImageField(upload_to='products/')
    discount = FloatField()
    price = FloatField()
    description = CharField(max_length=1000, blank=True, null=True)
    quick_overview = CharField(max_length=250, blank=True, null=True)
    quantity = IntegerField(default=1)

    def __str__(self):
        return self.title

class ProductToUser(BaseModel):
    product = ForeignKey(Product , CASCADE)
    user = ForeignKey(User , CASCADE)

class Blog(BaseModel):
    title = CharField(max_length=255)
    category = TreeForeignKey('app.BlogCategory', SET_NULL, blank=True, null=True)
    image = ImageField(upload_to='blogs/')
    description = CharField(max_length=1000, blank=True, null=True)
    quick_overview = CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title


class Category(MPTTModel):
    parent = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='children')
    name = CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Comment(MPTTModel, BaseModel):
    title = CharField(max_length=150)
    blog = ForeignKey(Blog, CASCADE, related_name="comments")
    parent = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='children')
    body = TextField()

    def __str__(self):
        return self.body


class BlogCategory(MPTTModel):
    parent = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='children')
    name = CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
