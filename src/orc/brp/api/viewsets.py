from rest_framework import viewsets

from ..models import NatuurlijkPersoon
from .serializers import NatuurlijkPersoonSerializer


class NatuurlijkPersoonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NatuurlijkPersoon.objects.all()
    serializer_class = NatuurlijkPersoonSerializer
    lookup_field = 'uuid'
