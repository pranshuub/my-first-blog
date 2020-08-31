from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.


class CV(models.Model):
    Name = models.CharField(max_length=200)
    dob = models.DateTimeField(default=timezone.now)
    email = models.CharField(max_length=200)
    phoneNo = models.CharField(max_length=15)
    profile = models.TextField()
    objective = models.TextField()
    SkillsAndA = models.TextField()
    education = models.TextField()
    workE = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Name
