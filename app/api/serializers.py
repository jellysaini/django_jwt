
import logging
from django.contrib.auth import authenticate

from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


logger = logging.getLogger(__name__)


class SerializerAPIAccountLogin(serializers.Serializer):
    """
    Represents login data.
    """

    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=30)

    def validate(self, attrs):

        try:
            self.email = attrs['email'].lower()
            self.user = User.objects.get(email=self.email)

        except (ObjectDoesNotExist, AttributeError):
            raise serializers.ValidationError(
                'Invalid email, Please check and try again.')

        if not self.user.check_password(attrs['password']):
            raise serializers.ValidationError(
                'Invalid password, Please check and try again.')

        return serializers.Serializer.validate(self, attrs)

    def login(self):

        login_user = authenticate(request=self.context['request'],
                                  username=self.validated_data['username'],
                                  password=self.validated_data['password'])

        refresh = RefreshToken.for_user(login_user)
        return {'token': str(refresh.access_token)}


class SerializerAPIAccountSignUp(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def validate_email(self, email):
        """
        Make sure emails are unique.
        """

        email = email.lower()

        try:
            User.objects.get(email=email)
            raise serializers.ValidationError(
                'Email {} already exists. Please choose another one.'.format(
                    email)
            )
        except ObjectDoesNotExist:
            return email

    def signup(self):
        user_data = {
            'username': self.validated_data.get('username'),
            'email': self.validated_data.get('email'),
            'password': self.validated_data.get('password'),
            'first_name': self.validated_data.get('first_name', ""),
            'last_name': self.validated_data.get('last_name', "")
        }

        user = User.objects.create_user(
            **user_data
        )
        refresh = RefreshToken.for_user(user)
        return {
            'id': user.id,
            'token': str(refresh.access_token)
        }


class SerializerAPIHome(serializers.Serializer):

    def save(self):
        return {'message': 'Hello World'}
