from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import integer_validator
from django.db.models import (
    FloatField, CharField, IntegerField, Model, ImageField, CASCADE, ForeignKey, EmailField, DateTimeField, SlugField,
    SET_NULL)
from django.utils.text import slugify


# User models
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

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = CharField(max_length=255)
    email = EmailField(unique=True)
    phone_number = CharField(max_length=25, validators=[integer_validator])
    address = CharField(max_length=255, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()



class Profile(Model):
    first_name = CharField(max_length=255, null=True)
    last_name = CharField(max_length=255, null=True)
    email = EmailField(max_length=255, null=True)
    heading = CharField(max_length=100, null=True)
    intro = CharField(max_length=500, null=True)


# Product models
class Product(BaseModel):
    title = CharField(max_length=255)
    category = ForeignKey('app.Category', SET_NULL, blank=True, null=True)
    discount = ForeignKey('app.Discount', SET_NULL, blank=True, null=True)
    gender = ForeignKey('app.Gender', SET_NULL, blank=True, null=True)
    colour = ForeignKey('app.Color', SET_NULL, blank=True, null=True)
    price = FloatField()
    description = CharField(max_length=1000, blank=True, null=True)
    quick_overview = CharField(max_length=250, blank=True, null=True)
    Quantity = IntegerField(default=1)

    def __str__(self):
        return self.title


class Image(Model):
    image = ImageField(upload_to='products/')
    product = ForeignKey('app.Product', CASCADE)


# Categories models
class Category(Model):
    parent = ForeignKey('app.Category', SET_NULL, blank=True, null=True)
    image = ImageField(upload_to='category/')
    name = CharField(max_length=255)
    slug = SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.name)
            while Category.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-1'

        super().save(force_insert, force_update, using, update_fields)


class Discount(Model):
    parent = ForeignKey('app.Discount', SET_NULL, blank=True, null=True)
    percent = CharField(max_length=255)
    slug = SlugField(unique=True)

    def __str__(self):
        return self.percent

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.percent)
            while Discount.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-1'

        super().save(force_insert, force_update, using, update_fields)


class Gender(Model):
    parent = ForeignKey('app.Gender', SET_NULL, blank=True, null=True)
    sex = CharField(max_length=255)
    slug = SlugField(unique=True)

    def __str__(self):
        return self.sex

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.sex)
            while Gender.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-1'

        super().save(force_insert, force_update, using, update_fields)


class Color(Model):
    parent = ForeignKey('app.Color', SET_NULL, blank=True, null=True)
    colour = CharField(max_length=255)
    slug = SlugField(unique=True)

    def __str__(self):
        return self.colour

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.colour)
            while Color.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-1'

        super().save(force_insert, force_update, using, update_fields)
