from rest_framework import viewsets

from orc.datamodel.models import NietNatuurlijkPersoon, VerblijfsObject

from .serializers import (
    NietNatuurlijkPersoonSerializer, VerblijfsObjectSerializer
)


class VerblijfsObjectViewSet(viewsets.ModelViewSet):
    queryset = VerblijfsObject.objects.all()
    serializer_class = VerblijfsObjectSerializer


class NietNatuurlijkPersoonViewSet(viewsets.ModelViewSet):
    queryset = NietNatuurlijkPersoon.objects.all()
    serializer_class = NietNatuurlijkPersoonSerializer
