from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_superuser', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **kwargs)
    
class Profile(AbstractBaseUser, PermissionsMixin):
    objects = AccountManager()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False)
    
    email = models.EmailField(unique=True, primary_key=True)
    username = models.CharField(max_length=40, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', default='profile_pictures/default.jpg')
    date_joined = models.DateTimeField(default=timezone.now)
    about_me = models.TextField(null=True, blank=True)  
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    

    def __str__(self):
        return self.email