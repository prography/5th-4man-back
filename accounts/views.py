from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.response import Response
from .serializers import SocialTokenObtainPairSerializer


class SocialTokenObtainPairView(TokenObtainPairView):
    serializer_class = SocialTokenObtainPairSerializer

    def get(self, request, *args, **kwargs):
        response = HttpResponseRedirect(redirect_to='http://example.com')
        response.set_cookie(key='hello', value='world')
        return response
