from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from .views import SocialTokenObtainAccessView, GithubOauthRedirectView, UserViewSet

user_router = routers.SimpleRouter()
user_router.register(r'', UserViewSet)

urlpatterns = [
    path('token/', SocialTokenObtainAccessView.as_view(), name='token_obtain_pair'),
    path('oauth/github/', GithubOauthRedirectView.as_view()),
]

urlpatterns += user_router.urls
