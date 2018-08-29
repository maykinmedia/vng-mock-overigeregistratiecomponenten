from rest_framework import viewsets

from ..models import MeldingOpenbareRuimte
from .serializers import MeldingOpenbareRuimteSerializer


class MeldingOpenbareRuimteViewSet(viewsets.ModelViewSet):
    queryset = MeldingOpenbareRuimte.objects.all()
    serializer_class = MeldingOpenbareRuimteSerializer
    lookup_field = 'uuid'
