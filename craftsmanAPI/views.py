from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Craftsman, Project, Review
from .serializers import CraftsmanSerializer,ProjectSerializer, ReviewSerializer


class CraftsmanViewSet(viewsets.ModelViewSet):
    # queryset = Craftsman.objects.all()
    serializer_class = CraftsmanSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Craftsman.objects.filter(user_id=int(user.id))
        return Response({'Fail': 'You have to be an authenticated user'}, status=status.HTTP_401_UNAUTHORIZED)

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