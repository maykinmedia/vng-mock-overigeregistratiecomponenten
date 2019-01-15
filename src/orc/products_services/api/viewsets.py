from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import ProductOfDienst
from .serializers import ProductOfDienstSerializer


class ProductOfDienstViewSet(ReadOnlyModelViewSet):
    queryset = ProductOfDienst.objects.all()
    serializer_class = ProductOfDienstSerializer
    lookup_field = 'uuid'
