from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.db.models import TextField
from django.db.transaction import atomic
from django.forms import Form, EmailField, CharField
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from social_core.pipeline import user

from app.models import User, Comment, ProductToUser
from app.tokens import account_activation_token
from root.settings import EMAIL_HOST, EMAIL_HOST_USER


class LoginForm(AuthenticationForm):
    username = CharField(required=False)
    email = EmailField()
    password = CharField(max_length=255)

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError('This email is not exists ')
        return email

    def clean_password(self):
        email = self.data.get('email')
        password = self.data.get('password')

        user = User.objects.filter(email=email).first()
        if user and not user.check_password(password):
            return ValidationError('Password entered error')
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
    confirm_password = CharField(max_length=255)

    def clean_email(self):
        email = self.data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(f' {email} this email is already registered ')
        return email

    def clean_username(self):
        username = self.data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError(f' User {username} is already registered ')
        return username

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Comfirm password is not same')
        return password

    @atomic
    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data.get('username'),
            email=self.cleaned_data.get('email')
        )
        user.set_password(self.cleaned_data.get('password'))
        user.save()


class ForgotPasswordForm(Form):
    email = EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError('This email is not registered ')
        return email


def send_email(email, request, _type):
    user = User.objects.get(email=email)
    subject = ' POLO Shop activate your account'
    current_site = get_current_site(request)
    message = render_to_string('app/auth/activation-password.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(str(user.pk))),
        'token': account_activation_token.make_token(user),
    })

    from_email = EMAIL_HOST_USER
    recipient_list = [email]

    result = send_mail(subject, message, from_email, recipient_list)
    print('Send to MAIL')


class CommentForm(Form):
    name = CharField(max_length=255)
    email = EmailField()
    comment = TextField()

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError(f'You are not registered')
        return email

    @atomic
    def save(self):
        comment = Comment.objects.create_comment(
            username=self.cleaned_data.get('title'),
            email=self.cleaned_data.get('email')
        )
        comment.save()

class ProductToUserAtomic:
    pass

    # @atomic
    # def save(self):
    #     product_to_user = ProductToUser.objects.create(
    #         pass
    #     )

