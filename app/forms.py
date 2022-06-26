from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.db.transaction import atomic
from django.forms import Form, EmailField, CharField

from app.models import User


class LoginForm(AuthenticationForm):
    email = EmailField()
    password = CharField(max_length=255)

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email):
            raise ValidationError('Bunday email mavjud emas')
        return email

    def clean_password(self):
        email = self.data.get('email')
        password = self.data.get('password')

        user = User.objects.get(email=email)

        if not user.check_password(password):
            return ValidationError('Parol xato')
        return password

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email is not None and password:
            self.user_cache = authenticate(
                self.request, email=email, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data


class RegisterForm(Form):
    username = CharField(max_length=255)
    email = EmailField()
    password = CharField(max_length=255)

    # confirm_password = CharField(max_length=255)

    def clean_email(self):
        email = self.data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(f'It is already registered by {email}')
        return email

    def clean_username(self):
        username = self.data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError(f'It is already registered by {username}')
        return username

    # TODO models ichiga UserManager classini yozasiz
    @atomic
    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data.get('username'),
            email=self.cleaned_data.get('email')
        )
        user.set_password(self.cleaned_data.get('password'))
        user.save()
