import logging
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import SerializerAPIAccountLogin, SerializerAPIAccountSignUp, SerializerAPIHome

logger = logging.getLogger(__name__)


class ViewAPIAccountLogin(APIView):

    permission_classes = (AllowAny,)
    serializer_class = SerializerAPIAccountLogin

    
    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance
        """
        return self.serializer_class(*args, **kwargs)

    
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


class ViewAPIAccountSignup(APIView):

    permission_classes = (AllowAny,)
    serializer_class = SerializerAPIAccountSignUp

    
    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance
        """
        return self.serializer_class(*args, **kwargs)

    
    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )

        if serializer.is_valid():
            response = serializer.signup()
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


class ViewAPIAccountHome(APIView):

    serializer_class = SerializerAPIHome


    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance
        """
        return self.serializer_class(*args, **kwargs)


    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(
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
            'status': 'success',
            'result': serializer.errors
        }
        return Response(data, status=HTTP_400_BAD_REQUEST)
