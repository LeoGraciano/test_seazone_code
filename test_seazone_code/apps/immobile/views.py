# Create your views here.
from apps.immobile.models import Immobile
from rest_framework import viewsets
from apps.immobile.serializers import ImmobileSerializer


class ImmobileViewSet(viewsets.ModelViewSet):
    queryset = Immobile.objects.all()
    serializer_class = ImmobileSerializer
