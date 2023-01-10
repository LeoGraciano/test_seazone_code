from apps.announcement.models import Announcement
from rest_framework import serializers


class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Announcement
        fields = [
            'id', 'platform_name', 'platform_tax', 'immobile', 'is_active', 'url'
        ]
