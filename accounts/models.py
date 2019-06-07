from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from accounts.managers import UserAccountManager
# Create your models here.

class UserAccount(AbstractUser):
    objects = models.Manager()
    user_objects = UserAccountManager()