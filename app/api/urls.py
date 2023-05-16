from django.urls import include, path
from .views import ViewAPIAccountLogin, ViewAPIAccountSignup, ViewAPIAccountHome


urlpatterns = [
    path('login/', ViewAPIAccountLogin.as_view(), name='login'),
    path('signup/', ViewAPIAccountSignup.as_view(), name='signup'),
    path('home/', ViewAPIAccountHome.as_view(), name='home'),
]
