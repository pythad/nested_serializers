from rest_framework import serializers

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class MyUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = MyUser
        fields = ('user', 'my_data')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(
            username=user_data['username'],
            email=user_data['email'],
            password=make_password(user_data['password'])
        )
        my_user = MyUser.objects.create(user=user, **validated_data)
        return my_user

    def update(self, instance, validated_data):

        instance.my_data = validated_data.get('my_data', instance.my_data)
        instance.save()

        user_data = validated_data.get('user')
        if user_data:
            user = instance.user
            user.username = user_data.get(
                'username',
                user.username
            )
            user.email = user_data.get(
                'email',
                user.email
            )
            new_password = user_data.get('password')
            user.password = make_password(new_password) if new_password else user.password

            user.save()

        return instance
