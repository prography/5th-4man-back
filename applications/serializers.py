from rest_framework import serializers
from rest_framework.fields import CreateOnlyDefault, CurrentUserDefault
from rest_framework.validators import UniqueTogetherValidator
from accounts.serializers import UserSerializer
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    applicant = UserSerializer(default=CreateOnlyDefault(CurrentUserDefault()))
    application_status = serializers.SerializerMethodField()

    class Meta:
        model = Application
        fields = (
            'id', 'team', 'applicant', 'reason', 'github_account', 'created_at', 'updated_at', 'application_status')
        read_only_fields = ('applicant',)
        validators = [
            UniqueTogetherValidator(
                queryset=Application.objects.all(),
                fields=['team', 'applicant']
            )
        ]

    def get_application_status(self, application):
        return application.get_status_display()
