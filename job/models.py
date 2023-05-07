from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db.models import TextChoices
# Create your models here.
from users.models import User


class JobStatusChoices(TextChoices):
    COMPLETED = 2
    PENDING = 1
    INPROGRESS = 3


class Job(models.Model):
    status = models.EmailField(null=True,blank=True, choices=JobStatusChoices.choices, default=JobStatusChoices.PENDING)
    title = models.CharField(max_length=300,null=True , blank=True)
    salary = models.CharField(max_length=1000 , null=True , blank=True)
    level = models.CharField(max_length=2000, null=True, blank=True,)
    vacancy = models.CharField(max_length=1000, null=True, blank=True)
    starting = models.CharField(max_length=1000, null=True, blank=True)
    duration = models.CharField(max_length=1000, null=True, blank=True)
    language = models.CharField(max_length=1000, null=True, blank=True)
    skill = models.CharField(max_length=1000, null=True, blank=True)
    location = models.CharField(max_length=1000, null=True, blank=True)
    map = models.CharField(max_length=1000, null=True, blank=True)
    overview = models.CharField(max_length=1000, null=True, blank=True)
    todo = models.CharField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="posted_jobs")

    class Meta:
        db_table = "job"

    def __str__(self):
        return self.title
