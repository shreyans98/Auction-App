from rest_framework import serializers
from .models import vendorProfile
class vendorProfileSerializer(serializers.ModelSerializer):
    vendor=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=vendorProfile
        fields='__all__'