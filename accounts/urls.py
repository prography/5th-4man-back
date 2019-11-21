from django.urls import path
from .views import SocialTokenObtainPairView, GithubOauthRedirectView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/', SocialTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('oauth/github', GithubOauthRedirectView.as_view()),
]
