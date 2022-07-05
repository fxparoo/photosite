from rest_framework import serializers
from photoapp.models import PhotoAlbum


class PhotoAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoAlbum
        fields = ['title', 'profile']
