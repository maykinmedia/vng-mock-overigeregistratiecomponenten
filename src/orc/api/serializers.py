from rest_framework import serializers

from orc.datamodel.models import DomeinData


class DomeinDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DomeinData
        fields = (
            'url',
            'data',
        )
