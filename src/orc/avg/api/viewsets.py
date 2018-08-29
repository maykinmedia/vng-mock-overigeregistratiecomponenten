from rest_framework import viewsets

from ..models import InzageVerzoek
from .serializers import InzageVerzoekSerializer


class InzageVerzoekViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InzageVerzoek.objects.all()
    serializer_class = InzageVerzoekSerializer
    lookup_field = 'uuid'
