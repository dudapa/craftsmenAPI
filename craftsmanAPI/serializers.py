from rest_framework.serializers import ModelSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from .models import Craftsman, Project, Visitor, Review, Skill


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']

class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']
    
class CraftsmanSerializer(ModelSerializer):
    skills = SkillSerializer(many=True, required=False)
    class Meta:
        model = Craftsman
        fields = ['id', 'user',  'name', 'email', 'phone', 'address', 'profile_picture', 'skills', 'created_at', 'updated_at']

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'craftsman', 'project_picture', 'created_at', 'updated_at']
    
class VisitorSerializer(ModelSerializer):
    class Meta:
        model = Visitor
        fields = ['id', 'user', 'name', 'email', 'profile_picture', 'created_at', 'updated_at']

class ReviewSerializer(ModelSerializer):
    class Meta: 
        model = Review
        fields = ['id', 'craftsman', 'author', 'rating', 'comment', 'created_at', 'updated_at']
