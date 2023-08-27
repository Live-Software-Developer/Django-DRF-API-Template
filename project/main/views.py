import random
from django.shortcuts import render, get_list_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework_bulk import BulkModelViewSet

from .authentication import AUTH_CLASS
from .models import Contact, BlogCategory, BlogTag, Blog, BlogReply, Review, Media
from .serializers import ContactSerializer, BlogCategorySerializer, BlogTagSerializer, BlogSerializer, \
    BlogReplySerializer, ReviewSerializer
from .extraserializers import MediaSerializer, StandardResultsSetPagination
from .utils import create_files


def home(request):
    # user = User.objects.create(username='lsd')
    # user.is_active = True
    # user.is_superuser = True
    # user.is_staff = True
    # user.set_password('!@#$%^&*')
    # user.save()
    return render(request, template_name='index.html', context={})


class ContactViewSet(viewsets.ModelViewSet):

    queryset = Contact.objects.get_queryset()
    serializer_class = ContactSerializer


class MediaViewSet(BulkModelViewSet):

    queryset = Media.objects.get_queryset()
    serializer_class = MediaSerializer

    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['type']
    search_fields = ['title']

    def create(self, request, *args, **kwargs):
        files = []
        for key, file in request.data.items():
            files.append(file)
        saved_files = create_files(files)
        data = self.serializer_class(saved_files, many=True).data
        return Response(data=data, status=201)


class BlogCategoryViewSet(BulkModelViewSet):

    queryset = BlogCategory.objects.get_queryset()
    serializer_class = BlogCategorySerializer

    authentication_classes = [AUTH_CLASS]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination


class BlogTagViewSet(BulkModelViewSet):

    queryset = BlogTag.objects.get_queryset()
    serializer_class = BlogTagSerializer

    authentication_classes = [AUTH_CLASS]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination


class BlogViewSet(viewsets.ModelViewSet):

    queryset = Blog.objects.get_queryset()
    serializer_class = BlogSerializer

    # authentication_classes = [AUTH_CLASS]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['tags__id', 'categories__id']
    search_fields = ['title', 'description', 'keywords']


class RandomBlogViewSet(viewsets.ModelViewSet):

    queryset = Blog.objects.get_queryset()
    serializer_class = BlogSerializer

    authentication_classes = [AUTH_CLASS]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['tags__id', 'categories__id']
    search_fields = ['title', 'description', 'keywords']

    @action(detail=False, methods=['GET'], url_path='get_random_blogs')
    def get_random_blogs(self, request):
        all_data = list(get_list_or_404(Blog))
        limit = request.query_params.get('limit', 10)
        num_entries = int(limit)
        if not (0 <= num_entries <= len(all_data)):
            num_entries = len(all_data)
        random_data = random.sample(all_data, num_entries)
        serializer = BlogSerializer(random_data, many=True, context={'request': request})
        return Response(serializer.data)


class BlogReplyViewSet(viewsets.ModelViewSet):

    queryset = BlogReply.objects.get_queryset()
    serializer_class = BlogReplySerializer


class ReviewViewSet(viewsets.ModelViewSet):

    queryset = Review.objects.get_queryset()
    serializer_class = ReviewSerializer
