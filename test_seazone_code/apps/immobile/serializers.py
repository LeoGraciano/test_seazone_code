from apps.immobile.models import Immobile
from rest_framework import serializers


class ImmobileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Immobile
        fields = [
            "id", 'code', "is_active", "active_at", 'limit_guests', "qty_bathrooms",
            "accept_pet", "cleaning_value", 'url',
        ]
