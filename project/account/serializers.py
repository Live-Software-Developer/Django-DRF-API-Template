from django.contrib.auth.hashers import make_password
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'user', 'phone_no']
        extra_kwargs = {
            'user': {
                "required": False
            }
        }


class AccountSerializer(WritableNestedModelSerializer):
    profile = ProfileSerializer(required=False)

    def validate_email(self, email):
        if self.instance is None and User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with this email already exists. You can reset your password",
                                              code='unique')
        return email

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'password', 'last_name', 'email', 'is_superuser', 'is_staff',
                  'is_active', 'date_joined', 'profile']
        extra_kwargs = {
            "password": {
                "write_only": True,
                "required": False
            },
            "is_superuser": {
                "read_only": True
            },
            "is_staff": {
                "read_only": True
            },
            "is_active": {
                "read_only": True
            },
            "date_joined": {
                "read_only": True
            }
        }

    def create(self, validated_data, *args, **kwargs):
        validated_data['password'] = make_password(validated_data.get('password', validated_data.get('username')))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        for key in list(validated_data.keys()):
            if key not in self.initial_data:
                validated_data.pop(key)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        self.fields['profile'] = ProfileSerializer(many=False)
        return super(AccountSerializer, self).to_representation(instance)

