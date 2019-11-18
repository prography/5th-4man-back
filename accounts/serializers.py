from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers, exceptions
from rest_framework_simplejwt import serializers as jwt_serializer
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class SocialTokenObtainSerializer(jwt_serializer.TokenObtainSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField(required=False)
        self.fields['password'] = jwt_serializer.PasswordField(required=False)
        self.fields['code'] = serializers.CharField(write_only=True, required=False)

    def validate(self, attrs):
        authenticate_kwargs = attrs
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)
        if self.user is None or not self.user.is_active:
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )

        return {}


class SocialTokenObtainPairSerializer(SocialTokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['is_new'] = False
        if not self.user.email and not self.user.nickname:
            data['is_new'] = True

        return data
