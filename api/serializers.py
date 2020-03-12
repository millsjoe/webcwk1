from django.contrib.auth.models import User, Group
from rest_framework import serializers

from modules.models import LecturerInfo, ModuleInfo, Rating


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, data):
        user = super(UserSerializer, self).create(data)
        user.set_password(data['password'])
        user.save()

        return user


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturerInfo
        fields = ['code', 'name']


class ModuleSerializer(serializers.ModelSerializer):
    taughtBy = LecturerSerializer(many=True)

    class Meta:
        model = ModuleInfo
        fields = ['code', 'title', 'year', 'semester', 'taughtBy']


# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']


class RatingSerializer(serializers.ModelSerializer):
    module = ModuleSerializer()

    class Meta:
        model = Rating
        fields = ['rating', 'lecturer', 'module']


# class LecturerRatingSerializer(serializers.ModelSerializer):


