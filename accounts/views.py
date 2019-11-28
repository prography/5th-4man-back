from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import SocialTokenObtainPairSerializer, UserSerializer
from .permissions import IsSelfOrReadCreateOnly
from rest_framework.permissions import AllowAny
User = get_user_model()


class SocialTokenObtainPairView(TokenObtainPairView):
    serializer_class = SocialTokenObtainPairSerializer


class GithubOauthRedirectView(APIView):
    def get(self, request, *args, **kwargs):
        response = HttpResponseRedirect(
            redirect_to='https://github.com/login/oauth/authorize?client_id=a7863c21770a0dd4c503')
        return response


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsSelfOrReadCreateOnly]
    permission_classes = [AllowAny]
    UNIQUE_FIELD = ['username', 'email', 'nickname']

    @action(methods=["post"], detail=False, url_path='check/duplication')
    def check_duplication(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = request.data
        response_data = dict()
        for key, value in data.items():
            if key not in self.UNIQUE_FIELD:
                continue
            is_duplicated = queryset.filter(**{key: value}).exists()
            response_data[key] = is_duplicated
        return Response(response_data)
