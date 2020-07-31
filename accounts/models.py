from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password):
        """
        Create a User model
        :param email:
        :param first_name:
        :param last_name:
        :param password:
        :return:
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must have a first name.')
        if not last_name:
            raise ValueError('Users must have a last name.')

        user = self.model(
            email=self.normalize_email(email=email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(raw_password=password)
        user.save(using=self._db)

    def create_superuser(self, email, first_name, last_name, password):
        """
        Create a super user
        :param email:
        :param first_name:
        :param last_name:
        :param password:
        :return:
        """
        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        user.is_admin = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Model representation for the custom user"""
    first_name = models.CharField(max_length=30, verbose_name="First name")
    last_name = models.CharField(max_length=30, verbose_name='Last name')
    email = models.EmailField(max_length=50, verbose_name='Email Address', unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name']

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



