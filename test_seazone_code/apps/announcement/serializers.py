from apps.announcement.models import Announcement
from rest_framework import serializers


class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
