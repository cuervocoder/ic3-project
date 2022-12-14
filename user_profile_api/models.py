from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(
        self, 
        email, 
        first_name, 
        last_name, 
        profile_type,
        password=None
    ):
        if not email:
            raise ValueError('User must have an email!')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            profile_type=profile_type
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self, 
        email,
        password
    ):
        user = self.create_user(
            email,
            'superadmin',
            'superadmin',
            UserProfileType.objects.get(description = 'SUPERADMIN'),
            password
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.TextField(max_length=100, null=True)
    last_name = models.TextField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profile_type = models.ForeignKey("UserProfileType", on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'

class UserProfileType(models.Model):
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.description
