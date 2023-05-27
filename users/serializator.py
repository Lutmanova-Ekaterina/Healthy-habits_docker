from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (  # fields обязательный - Список или кортеж имен полей, которые должны составлять уникальный набор. Они должны существовать как поля в классе сериализатора.
            'email',
            'password',
        )

    def create(self, validated_data):
        """переопределим, чтобы хешировался пвроль"""
        return User.objects.create(email=validated_data['email'], password=make_password(validated_data['password']))
