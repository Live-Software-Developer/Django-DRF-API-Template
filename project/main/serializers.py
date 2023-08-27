from rest_framework import serializers
from account.serializers import AccountSerializer
from rest_framework_bulk import BulkSerializerMixin

from .models import Contact, BlogCategory, BlogTag, Blog, BlogReply, Review
from .utils import BaseSerializer


class ContactSerializer(BaseSerializer, serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class BlogCategorySerializer(BaseSerializer, serializers.ModelSerializer):

    class Meta:
        model = BlogCategory
        fields = ['id', 'title', 'slug', 'created_on']


class BlogTagSerializer(BaseSerializer, BulkSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = BlogTag
        fields = ['id', 'title', 'slug', 'created_on']


class BlogReplySerializer(BaseSerializer, serializers.ModelSerializer):

    class Meta:
        model = BlogReply
        fields = ['id', 'user', 'blog', 'details']

    def to_representation(self, instance):
        self.fields['user'] = AccountSerializer(many=True)
        return super(BlogReplySerializer, self).to_representation(instance)


class BlogSerializer(BaseSerializer, serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'user', 'title', 'slug', 'description', 'keywords', 'categories', 'tags',
                  'details', 'image', 'image_alt_text', 'replies', 'created_on', 'modified_on']
        extra_kwargs = {
            'replies': {
                'required': False
            }
        }

    def to_representation(self, instance):
        fields = self.get_fields()
        required_fields = set(fields.keys())
        if 'user' in required_fields:
            self.fields['user'] = AccountSerializer(many=False)
        if 'categories' in required_fields:
            self.fields['categories'] = BlogCategorySerializer(many=True)
        if 'tags' in required_fields:
            self.fields['tags'] = BlogTagSerializer(many=True)
        if 'replies' in required_fields:
            self.fields['replies'] = BlogReplySerializer(many=True)
        return super(BlogSerializer, self).to_representation(instance)

    def update(self, instance, validated_data):

        for key in list(validated_data.keys()):
            if key not in self.initial_data:
                validated_data.pop(key)
        return super().update(instance, validated_data)


class ReviewSerializer(BaseSerializer, serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'user', 'review', 'rating', 'created_on']

    def to_representation(self, instance):
        self.fields['user'] = AccountSerializer(many=False)
        return super(ReviewSerializer, self).to_representation(instance)
