from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Skill(models.Model):
    name = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Craftsman(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='images/craftsmen/', null=True, blank=True)
    skills = models.ManyToManyField(Skill)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'craftsmen'

    def __str__(self):
        return f'{self.user.first_name} '
    
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    craftsman = models.ForeignKey(Craftsman, on_delete=models.CASCADE)
    project_picture = models.ImageField(upload_to='images/projects/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    craftsman = models.ForeignKey(Craftsman, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.author} {self.rating}'