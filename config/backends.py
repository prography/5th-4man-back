from django.contrib.auth import get_user_model
from accounts.utils import get_github_access_token, get_github_user_json
from accounts.models import GithubProfile

GITHUB_USERNAME_PREFIX = 'github_'
User = get_user_model()


class GithubBackend:
    def authenticate(self, request, code=None, **kwargs):
        response = get_github_access_token(code)
        if 'error' in response:
            return
        access_token = response['access_token']
        github_user_json = get_github_user_json(access_token)

        profile_id = github_user_json['id']
        login = github_user_json['login']
        defaults = {
            'avatar': github_user_json['avatar_url'],
            'email': github_user_json['email'],
            'login': github_user_json['login']
        }
        profile, is_new = GithubProfile.objects.update_or_create(id=profile_id, defaults=defaults)
        if is_new:
            user = User.objects._create_user(username=GITHUB_USERNAME_PREFIX + login, email=None, password=None,
                                             profile=profile)
        else:
            user = profile.user
        return user
