from django.conf import settings
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Media


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'limit'
    page_query_param = 'page'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })


class MediaSerializer(serializers.ModelSerializer):
    media_url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ['id', 'file', 'title', 'type', 'media_url']

        extra_kwargs = {
            'image_url': {
                'required': False
            }
        }

    def get_media_url(self, obj):
        return f""
