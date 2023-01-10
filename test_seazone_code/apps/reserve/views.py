# Create your views here.
from apps.reserve.models import Reserve
from rest_framework import viewsets, mixins
from apps.reserve.serializers import ReserveSerializer


class ReserveViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer
