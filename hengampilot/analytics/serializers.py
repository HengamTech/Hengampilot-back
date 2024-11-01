from rest_framework import serializers
from .models import AuditLog

class AuditLogSerializer(serializers.ModelSerializer):
    content_type = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = AuditLog
        fields = '__all__'