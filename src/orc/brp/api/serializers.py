from rest_framework import serializers

from ..models import NatuurlijkPersoon


class NatuurlijkPersoonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NatuurlijkPersoon
        fields = (
            'url',
            'bsn',
            'naam',
            'telefoonnummer',
            'email',
        )
        extra_kwargs = {
            'url': {
                'lookup_field': 'uuid',
            }
        }
