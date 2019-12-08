from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'team', 'applicant', 'reason', 'github_account', 'created_at', 'updated_at',)
        read_only_fields = ('applicant',)
