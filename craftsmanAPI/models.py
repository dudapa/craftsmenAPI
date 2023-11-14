from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Craftsman(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    profile_picture = models.ImageField()
    skills = models.ManyToManyField(Skill)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    craftsman = models.ForeignKey(Craftsman, on_delete=models.CASCADE)
    project_picture = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title