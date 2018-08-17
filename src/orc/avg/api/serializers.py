from rest_framework import serializers

from ..models import InzageVerzoek


class InzageVerzoekSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InzageVerzoek
        fields = (
            'uuid',
            'inzage_wmo',
            'inzage_jeugd',
            'inzage_participatie',
            'inzage_veiligheidskamer',
            'inzage_schuldhulpverlening',
            'inzage_overige_regelingen',
            'onderwerp_overige_regelingen',
            'inzage_algemeen',
            'reden_inzage_algemeen',
            'antwoord_per_email',
        )
        extra_kwargs = {
            'url': {
                'lookup_field': 'uuid',
            }
        }
