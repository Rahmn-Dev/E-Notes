from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ReadOnlyField
from . import models

class notes(serializers.ModelSerializer):

    class Meta:
        model = models.Note
        fields = [
            "title",
            "content",
            "created_at",
            "updated_at",
            "trashed",
        ] 