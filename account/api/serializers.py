import logging

from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from account.models import ModelAccountUser


logger = logging.getLogger(__name__)


# -------------------------------------------------------------------------------
# SerializerAccountUser
# -------------------------------------------------------------------------------
class SerializerAccountUser(serializers.ModelSerializer):
    """
    Resents API data for a user.
    """

    # ---------------------------------------------------------------------------
    # Meta
    # ---------------------------------------------------------------------------
    class Meta:
        model = ModelAccountUser
        fields = ('id', 'email', 'first_name',
                  'last_name', 'uid', 'is_active',)


# ---------------------------------------------------------------
# SerializerAccountSignUp
# ---------------------------------------------------------------
class SerializerAccountSignUp(serializers.Serializer):

    """
    Register as User
    """

    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=60)
    first_name = serializers.CharField(max_length=60)
    last_name = serializers.CharField(max_length=60)

    #  ---------------------------------------------------------------
    # validate_email
    #  ---------------------------------------------------------------
    def validate_email(self, email):
        """
        Make sure emails are unique.
        """

        email = email.lower()

        try:
            ModelAccountUser.objects.get(email=email)
            raise serializers.ValidationError(
                'Email {} already exists. Please choose another one.'.format(
                    email)
            )
        except ObjectDoesNotExist:
            return email

    #  ---------------------------------------------------------------
    # save
    #  ---------------------------------------------------------------

    def save(self):

        user_data = {
            'email': self.validated_data.get('email'),
            'password': self.validated_data.get('password'),
            'first_name': self.validated_data.get('first_name'),
            'last_name': self.validated_data.get('last_name'),
        }

        user = ModelAccountUser.objects.signup_process(
            user_data
        )

        return SerializerAccountUser(user).data


# ---------------------------------------------------------------
# SerializerAPIAccountLogin
# ---------------------------------------------------------------
class SerializerAPIAccountLogin(serializers.Serializer):
    """
    Represents login data.
    """

    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=30)

    # ---------------------------------------------------------------
    # validate
    # ---------------------------------------------------------------

    def validate(self, attrs):

        try:
            email = attrs['email'].lower()
            self.user = ModelAccountUser.objects.get(email=email)

        except (ObjectDoesNotExist, AttributeError):
            raise serializers.ValidationError(
                'Invalid email, Please check and try again.')

        if not self.user.check_password(attrs['password']):
            raise serializers.ValidationError(
                'Invalid password, Please check and try again.')

        return serializers.Serializer.validate(self, attrs)

    # ---------------------------------------------------------------
    # login
    # ---------------------------------------------------------------
    def login(self):
        login_user = ModelAccountUser.objects.login_user(
            self.user, self.context['request'],
            self.validated_data['password']
        )

        return login_user


# ---------------------------------------------------------------
# SerializerAPIAccountLogin
# ---------------------------------------------------------------
class SerializerAPIAccountMe(serializers.Serializer):
    """
    Represents logged in user.
    """
    pass

    # ---------------------------------------------------------------
    # login
    # ---------------------------------------------------------------
    def me(self):
        user = self.context['request'].user
        return SerializerAccountUser(user).data