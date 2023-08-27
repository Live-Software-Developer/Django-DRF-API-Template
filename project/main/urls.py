from django.urls import path, include
from rest_framework import routers

from .views import home, MediaViewSet, ContactViewSet, BlogCategoryViewSet, BlogTagViewSet, \
    BlogViewSet, BlogReplyViewSet, ReviewViewSet, RandomBlogViewSet

router = routers.DefaultRouter()
router.register(r'media', MediaViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'blogs/blog-categories', BlogCategoryViewSet)
router.register(r'blogs/blog-tags', BlogTagViewSet)
router.register(r'blogs/blog-replies', BlogReplyViewSet)
router.register(r'blogs/random-blogs', RandomBlogViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls))
]
