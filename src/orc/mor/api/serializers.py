from rest_framework import serializers

from ..models import MeldingOpenbareRuimte


class MeldingOpenbareRuimteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MeldingOpenbareRuimte
        fields = (
            'url',
            'hoofdcategorie',
            'subcategorie',
            'locatie_beschrijving',
            'data',
        )
        extra_kwargs = {
            'url': {
                'lookup_field': 'uuid',
            }
        }
