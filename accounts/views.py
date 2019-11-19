from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import SocialTokenObtainPairSerializer, UserSerializer

User = get_user_model()


class SocialTokenObtainPairView(TokenObtainPairView):
    serializer_class = SocialTokenObtainPairSerializer

    def get(self, request, *args, **kwargs):
        response = HttpResponseRedirect(redirect_to='http://example.com')
        response.set_cookie(key='hello', value='world')
        return response


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        UserSerializer(partial=True)
        pass
