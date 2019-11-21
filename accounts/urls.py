from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from .views import SocialTokenObtainPairView, GithubOauthRedirectView, UserViewSet

user_router = routers.SimpleRouter()
user_router.register(r'', UserViewSet)

urlpatterns = [
    path('token/', SocialTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('oauth/github/', GithubOauthRedirectView.as_view()),
]

urlpatterns += user_router.urls
