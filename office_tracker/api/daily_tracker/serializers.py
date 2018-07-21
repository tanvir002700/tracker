from rest_framework import serializers
from daily_tracker.models import Attandance


class AttandanceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    enter_at = serializers.DateTimeField(allow_null=True)
    out_at = serializers.DateTimeField(allow_null=True)
    total_time = serializers.IntegerField(default=0)

    def create(self, validated_data):
        return Attandance.object.create(**validated_data)

    def update(self, instance, validated_data):
        return instance
