from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import SocialTokenObtainPairSerializer


class SocialTokenObtainPairView(TokenObtainPairView):
    serializer_class = SocialTokenObtainPairSerializer
