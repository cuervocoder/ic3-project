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
        dni,
        address,
        phone,
        emergency_phone,
        auto_increment_id,
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
            dni=dni,
            address=adress,
            phone=phone,
            emergency_phone=emergency_phone,
            auto_increment_id=auto_increment_id,
            profile_type=profile_type
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self, 
        email,
        password,
        auto_increment_id,
        phone,
        emergency_phone
    ):
        user = self.create_user(
            email,
            auto_increment_id,
            phone,
            emergency_phone,
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
    dni = models.CharField(max_length=100, unique=True, null=True)
    auto_increment_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    address = models.TextField(max_length=100, null=True)
    phone = models.TextField(max_length=100, null=True)
    emergency_phone = models.TextField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profile_type = models.ForeignKey('UserProfileType', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['auto_increment_id', 'phone', 'emergency_phone']

class UserProfileType(models.Model):
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.description
