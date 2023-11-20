from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import Craftsman, Project, Review
from .serializers import CraftsmanSerializer,ProjectSerializer, ReviewSerializer


class CraftsmanViewSet(viewsets.ModelViewSet):
    queryset = Craftsman.objects.all()
    serializer_class = CraftsmanSerializer

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