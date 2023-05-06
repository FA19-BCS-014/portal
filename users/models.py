from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db.models import TextChoices
# Create your models here.


class UserTypeChoices(TextChoices):
    COMPANY = 2
    USER = 1


class User(AbstractUser):
    email = models.EmailField(null=True,blank=True,unique=True)
    username = models.CharField(max_length=300,null=True , blank=True)
    password = models.CharField(max_length=1000 , null=True , blank=True)
    user_type = models.CharField(max_length=2000, null=True, blank=True, choices=UserTypeChoices.choices)

    REQUIRED_FIELDS = []

    USERNAME_FIELD = 'email'

    login_token = models.TextField(null=True, blank=True)
    last_login = models.DateTimeField(null=True,blank=True)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.email
