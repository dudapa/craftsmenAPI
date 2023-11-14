from django.contrib import admin
from .models import Craftsman, Project, Review, Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
# Register your models here.
@admin.register(Craftsman)
class CraftsmanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'craftsman')

@admin.register(Review)
class ReviewModel(admin.ModelAdmin):
    list_display = ('id', 'craftsman', 'author', 'rating')