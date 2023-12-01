from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .models import Craftsman, Project, Review, Skill
from .serializers import CraftsmanSerializer,ProjectSerializer, ReviewSerializer, SkillSerializer
from .permissions import IsAdminAndCraftsmanOrReadOnly, OnlyCraftsman


class CraftsmanViewSet(viewsets.ModelViewSet):
    # queryset = Craftsman.objects.all()
    serializer_class = CraftsmanSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'POST':
            return [OnlyCraftsman()]
        return [IsAdminAndCraftsmanOrReadOnly()] 

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and not user.is_staff:
            return Craftsman.objects.filter(user_id=int(user.id))
        return Craftsman.objects.all()

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(craftsman_id=self.kwargs['craftsman_pk'])

    def get_serializer_context(self):
        return {'craftsman_id': self.kwargs['craftsman_pk']}
    

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(craftsman_id=self.kwargs['craftsman_pk'])

    def get_serializer_context(self):
        return {'craftsman_id': self.kwargs['craftsman_pk']}

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer