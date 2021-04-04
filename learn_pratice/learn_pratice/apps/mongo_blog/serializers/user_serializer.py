
from learn_pratice.apps.mongo_blog.models.mongodb.user import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')