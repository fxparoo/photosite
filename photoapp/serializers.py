from rest_framework import serializers
from photoapp.models import PhotoRepo


class PhotoRepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoRepo
        fields = ['title', 'profile']
