
from learn_pratice.apps.mongo_blog.models.mongodb.user import User
from learn_pratice.apps.mongo_blog.serializers.user_serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import (viewsets, status)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET', 'POST'])
def user_list(request, format=None):
    print('---------------user_list--------------------')
    users = User.objects.all()
    if request.method == 'GET':
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

