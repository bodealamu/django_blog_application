from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User, AbstractUser


class CustomUserManager(BaseUserManager):
    pass


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Model representation for the custom user"""
    first_name = models.CharField(max_length=30, verbose_name="First name")
    last_name = models.CharField(max_length=30, verbose_name='Last name')
    email = models.EmailField(max_length=50, verbose_name='Email Address')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_full_name(self):
        firstname = self.first_name
        lastname = self.last_name
        fullname = str(firstname) + ' ' + str(lastname)
        return  fullname

    def get_short_name(self):
        return self.first_name



