from rest_framework import serializers

from orc.datamodel.models import Adres, VerblijfsObject, NietNatuurlijkPersoon


class AdresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adres
        fields = (
            'id',
            'straatnaam',
            'postcode',
            'woonplaatsnaam',
            'huisnummer',
            'huisletter',
            'huisnummertoevoeging',
        )


class VerblijfsObjectSerializer(serializers.HyperlinkedModelSerializer):
    hoofdadres = AdresSerializer()

    class Meta:
        model = VerblijfsObject
        fields = (
            'url',
            'identificatie',
            'hoofdadres',
        )

    def create(self, validated_data):
        adres, _ = Adres.objects.get_or_create(validated_data['hoofdadres'])
        validated_data['hoofdadres'] = adres
        return VerblijfsObject.objects.create(**validated_data)


class NietNatuurlijkPersoonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NietNatuurlijkPersoon
        fields = (
            'url',

            'rsin',
            'statutaire_naam',
            'datum_aanvang',
            'datum_beeindiging',
        )
        extra_kwargs = {
            'url': {
                'lookup_field': 'uuid',
            }
        }
