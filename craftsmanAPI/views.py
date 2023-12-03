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

    def create(self, request, *args, **kwargs):
        data = request.data[0]
        user = request.user
        new_craftsman = Craftsman.objects.create(user=user, name=data['name'], email=data['email'], phone=data['phone'], address=data['address'], profile_picture=data['profile_picture'])
        new_craftsman.save()
        
        for skill in data['skills']:
            skill_obj = Skill.objects.get(name=skill['name'])
            new_craftsman.skills.add(skill_obj)
        
        serializer = CraftsmanSerializer(new_craftsman)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        craftsman = self.get_object()
        data = request.data[0]
        print(data)
        craftsman.skills.set([])
        for skill in data['skills']:
            skill_obj = Skill.objects.get(name=skill['name'])
            craftsman.skills.add(skill_obj)
            print('it works2')

        craftsman.save()
        serializer = CraftsmanSerializer(craftsman)
        return Response(serializer.data, status=status.HTTP_200_OK)


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