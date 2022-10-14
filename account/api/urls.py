from django.urls import path
from account.api.views import ViewAPIAccountSignUp,ViewAPIAccountLogin, ViewAPIAccountMe

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [

    path('signup/',
         ViewAPIAccountSignUp.as_view(),
         name='signup'
         ),

    path('login/',
         ViewAPIAccountLogin.as_view(),
         name='login'
         ),

    path('me/',
         ViewAPIAccountMe.as_view(),
         name='me'
         ),

    path('token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),

    path('token/verify/',
         TokenVerifyView.as_view(),
         name='token_verify'),
]
