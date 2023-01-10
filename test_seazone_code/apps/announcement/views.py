# Create your views here.
from apps.announcement.models import Announcement
from rest_framework import viewsets, mixins
from apps.announcement.serializers import AnnouncementSerializer


class AnnouncementViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
