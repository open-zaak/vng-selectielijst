from rest_framework import serializers

from selectielijst.datamodel.models import (
    CommunicatieKanaal,
    ResultaattypeOmschrijvingGeneriek,
)


class CommunicatieKanaalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommunicatieKanaal
        fields = ("url", "naam", "omschrijving")
        extra_kwargs = {"url": {"lookup_field": "uuid"}}
