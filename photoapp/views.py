from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from photoapp.models import PhotoAlbum
from photoapp.serializers import PhotoAlbumSerializer
from rest_framework.pagination import PageNumberPagination


class PhotoAlbumViewSet(viewsets.ViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def list(self, request):
        queryset = PhotoAlbum.objects.all()
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = PhotoAlbumSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = PhotoAlbumSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = PhotoAlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = PhotoAlbum.objects.all()
        photo = get_object_or_404(queryset, pk=pk)
        serializer = PhotoAlbumSerializer(photo)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            queryset = PhotoAlbum.objects.all()
            photo = get_object_or_404(queryset, pk=pk)
            if photo.delete():
                return Response({"detail": "Photo deleted Succesfully."}, status=status.HTTP_204_NO_CONTENT)
        except PhotoAlbum.DoesNotExist:
            return Response({"detail": "Photo can't be found."}, status=status.HTTP_400_BAD_REQUEST)
