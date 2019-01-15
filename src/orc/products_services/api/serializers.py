from rest_framework.serializers import HyperlinkedModelSerializer

from ..models import ProductOfDienst


class ProductOfDienstSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ProductOfDienst
        fields = ('url', 'naam', 'omschrijving', 'webpagina')
        extra_kwargs = {
            'url': {
                'lookup_field': 'uuid',
            }
        }
