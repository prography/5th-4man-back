import requests
import json
from django.conf import settings

GITHUB_ACCESS_TOKEN_URL = "https://github.com/login/oauth/access_token/"
GITHUB_USER_URL = "https://api.github.com/user"


def get_github_access_token(code):
    """
    ex) response
    {
    "access_token": "56470bfebe1af2c5b8da3cc61cc7b23bd78d1b38",
    "token_type": "bearer",
    "scope": ""
    }

    ex) error
    {
    'error': 'bad_verification_code',
    'error_description': 'The code passed is incorrect or expired.',
    'error_uri': 'https://developer.github.com/apps/managing-oauth-apps/troubleshooting-oauth-app-access-token-request-errors/#bad-verification-code'
    }

    """
    headers = {
        'Accept': 'application/json; charset=utf-8',
    }
    body = {
        "client_id": settings.SOCIAL_AUTH_GITHUB_KEY,
        "client_secret": settings.SOCIAL_AUTH_GITHUB_SECRET,
        "code": code,
    }
    response = requests.post(GITHUB_ACCESS_TOKEN_URL, data=body, headers=headers)

    return response.json()


def get_github_user_json(access_token):
    """
    ex) error
    {
    "message": "Bad credentials",
    "documentation_url": "https://developer.github.com/v3"
    }
    """
    headers = {
        'Accept': 'application/json; charset=utf-8',
        'Authorization': 'token ' + access_token
    }
    response = requests.get(GITHUB_USER_URL, headers=headers)
    return response.json()
