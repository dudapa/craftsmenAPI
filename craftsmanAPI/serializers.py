from rest_framework.serializers import ModelSerializer
from .models import Craftsman, Project, Review, Skill


class Skill(ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'created_at', 'updated_at']
    
class CraftsmanSerializer(ModelSerializer):
    class Meta:
        model = Craftsman
        fields = ['id', 'name', 'email', 'phone', 'address', 'profile_picture', 'skills', 'created_at', 'updated_at']

class Project(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'craftsman', 'project_picture', 'created_at', 'updated_at']

class Review(ModelSerializer):
    class Meta: 
        model = Review
        fields = ['id', 'craftsman', 'author', 'rating', 'comment', 'created_at']