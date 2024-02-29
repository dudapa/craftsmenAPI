from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from .models import Craftsman, Project, Review, Skill, Visitor
from .serializers import CraftsmanSerializer,ProjectSerializer, ReviewSerializer, SkillSerializer, VisitorSerializer
from .permissions import IsAdminOrCraftsmanOrReadOnly, OnlyCraftsman, OnlyAdmin, OnlyAuthenticatedVisitor, IsAdminOrAuthenticatedVisitor


class CraftsmanViewSet(viewsets.ModelViewSet):
    serializer_class = CraftsmanSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'POST':
            return [OnlyCraftsman()]
        return [IsAdminOrCraftsmanOrReadOnly()] 

    def get_queryset(self):
        try:
            user = self.request.user
            if not user.is_anonymous:
                return Craftsman.objects.filter(user=user)
            return Craftsman.objects.all()
        except ObjectDoesNotExist:
            return Craftsman.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            user = request.user
            new_craftsman = Craftsman.objects.create(
                user=user, 
                name=data['name'], 
                email=data['email'], 
                phone=data['phone'], 
                address=data['address'], 
                profile_picture=data.get('profile_picture', None)
                )
            new_craftsman.save()

            # Add skills to new craftsman
            for skill in data['skills']:
                skill_obj = Skill.objects.get(name=skill)
                new_craftsman.skills.add(skill_obj)

            # Assign craftsman group to user
            craftsman_group = Group.objects.get(name='craftsman')
            user.groups.add(craftsman_group)
            
            serializer = CraftsmanSerializer(new_craftsman)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({'detail': 'You have already created craftsman profile'}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        craftsman = get_object_or_404(Craftsman, user=request.user)
        data = request.data

        skills = None
        if 'skills' in data:
            skills = data.pop('skills')
            craftsman.skills.set([])
            for skill in skills:
                skill_obj = Skill.objects.get(name=skill)
                craftsman.skills.add(skill_obj)

            craftsman.save()

        serializer = CraftsmanSerializer(craftsman, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'POST':
            return [OnlyCraftsman()]
        return [IsAdminAndCraftsmanOrReadOnly()] 

    def get_queryset(self):
        return Project.objects.filter(craftsman_id=self.kwargs['craftsman_pk'])

    def get_serializer_context(self):
        return {'craftsman_id': self.kwargs['craftsman_pk']}
    
    def create(self, request, *args, **kwargs):
        craftsman_id = self.kwargs['craftsman_pk']
        craftsman = Craftsman.objects.get(pk=craftsman_id)
        data = request.data
        new_project = Project.objects.create(
               title=data['title'],
               description=data.get('description', None),
               craftsman=craftsman,
               project_picture=data.get('project_picture', None)
        )
        new_project.save()
        serializer = ProjectSerializer(new_project)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'POST':
            return [OnlyAuthenticatedVisitor()]
        return [AllowAny()] 

    def get_queryset(self):
        return Review.objects.filter(craftsman_id=self.kwargs['craftsman_pk'])

    def get_serializer_context(self):
        return {'craftsman_id': self.kwargs['craftsman_pk']}

class VisitorViewSet(viewsets.ModelViewSet):
    serializer_class = VisitorSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_permissions(self):

        if self.request.method == 'POST':
            return [IsAuthenticated()]
        elif self.request.method == 'PUT':
            return [OnlyAuthenticatedVisitor()]
        else:
            return [IsAdminOrAuthenticatedVisitor()]
        
    def get_queryset(self):
        try:
            user = self.request.user
            Visitor.objects.filter(user=user)
            return Visitor.objects.all()
        except ObjectDoesNotExist:
            return Visitor.objects.all()
        
    def create(self, request, *args, **kwargs):
        user = self.request.user
        if not user.is_anonymous and not user.is_staff:
            data = request.data
            data['user'] = user.id
            serializer = VisitorSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
            

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [OnlyAdmin]