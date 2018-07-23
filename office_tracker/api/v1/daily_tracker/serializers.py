from rest_framework import serializers
from daily_tracker.models import Attandance


class AttandanceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:attandance-detail')
    class Meta:
        model = Attandance
        fields = ('id', 'enter_at', 'out_at', 'total_time', 'url')
