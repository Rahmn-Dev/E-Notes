from rest_framework import generics, status, viewsets, permissions, filters
from . import serializers
from . import models
# import django_filters.rest_framework

class notesApiViewSet(viewsets.ModelViewSet):

    queryset = models.Note.objects.all()
    serializer_class = serializers.notes
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]