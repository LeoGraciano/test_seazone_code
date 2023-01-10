from datetime import timedelta
from apps.reserve.models import Reserve
from rest_framework import serializers
from django.utils.translation import ugettext as _
from django.utils import timezone


class ReserveSerializer(serializers.HyperlinkedModelSerializer):

    def validate_check_in(self, attrs):
        if attrs < timezone.now().date():
            raise serializers.ValidationError(
                _('Data de check-in inválida')
            )

        return attrs

    def validate_check_out(self, attrs):
        if attrs < (timezone.now() + timedelta(days=1)).date():
            raise serializers.ValidationError(
                _('Data de check-out inválida')
            )

        return attrs

    def validate(self, attrs):

        if attrs['check_in'] >= attrs['check_out']:
            raise serializers.ValidationError(
                _('Data de check-in igual ou superior ao check-out')
            )

        return attrs

    class Meta:
        model = Reserve
        fields = [
            "id", "code", "check_in", "check_out", "price_total",
            "comment", "number_quests", "is_active", "url", "announcement"
        ]
