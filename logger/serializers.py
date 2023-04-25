from rest_framework import serializers
from .models import i18nLog


class i18nLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = i18nLog
        fields = "__all__"
