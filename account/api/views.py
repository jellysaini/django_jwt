import logging

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.generics import get_object_or_404

from account.api.serializers import SerializerAccountSignUp, SerializerAPIAccountLogin,  SerializerAPIAccountMe
from account.models import ModelAccountUser

logger = logging.getLogger(__name__)




# ---------------------------------------------------------------
# ViewAPIAccountSignUp
# ---------------------------------------------------------------
class ViewAPIAccountSignUp(APIView):
    """
    API view for sign up 
    """

    permission_classes = (AllowAny, )
    serializer_class = SerializerAccountSignUp


    # ---------------------------------------------------------------
    # get_serializer
    # ---------------------------------------------------------------
    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance
        """
        return SerializerAccountSignUp(*args, **kwargs)


    # ---------------------------------------------------------------
    # post
    # ---------------------------------------------------------------
    def post(self, request, *args, **kwargs):

        serializer = SerializerAccountSignUp(
            data=request.data,
            context={'request': request}
        )

        if serializer.is_valid():
            response = serializer.save()
            data = {
                'code': 200,
                'status': 'success',
                'result': response
            }
            return Response(data, status=HTTP_200_OK)

        data = {
            'code': 400,
            'status': 'error',
            'result': serializer.errors
        }
        return Response(data, status=HTTP_400_BAD_REQUEST)




# ---------------------------------------------------------------
# ViewAPIAccountLogin
# ---------------------------------------------------------------
class ViewAPIAccountLogin(APIView):

    permission_classes = (AllowAny,)
    serializer_class = SerializerAPIAccountLogin


    # ---------------------------------------------------------------
    # get_serializer
    # ---------------------------------------------------------------
    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance
        """
        return SerializerAPIAccountLogin(*args, **kwargs)


    # ---------------------------------------------------------------
    # post
    # ---------------------------------------------------------------
    def post(self, request, *args, **kwargs):

        logger.debug('Attempting to login a user.')

        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )

        if serializer.is_valid():
            response = serializer.login()
            data = {
                'code': 200,
                'status': 'success',
                'result': response
            }
            return Response(data, status=HTTP_200_OK)
        data = {
            'code': 400,
            'status': 'success',
            'result': serializer.errors
        }
        return Response(data, status=HTTP_400_BAD_REQUEST)


# ---------------------------------------------------------------
# ViewAPIAccountMe
# ---------------------------------------------------------------
class ViewAPIAccountMe(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SerializerAPIAccountMe


    # ---------------------------------------------------------------
    # get_serializer
    # ---------------------------------------------------------------
    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance
        """
        return SerializerAPIAccountMe(*args, **kwargs)


    # ---------------------------------------------------------------
    # post
    # ---------------------------------------------------------------
    def post(self, request, *args, **kwargs):


        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )

        if serializer.is_valid():
            response = serializer.me()
            data = {
                'code': 200,
                'status': 'success',
                'result': response
            }
            return Response(data, status=HTTP_200_OK)
        data = {
            'code': 400,
            'status': 'success',
            'result': serializer.errors
        }
        return Response(data, status=HTTP_400_BAD_REQUEST)