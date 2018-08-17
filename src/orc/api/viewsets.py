from rest_framework import viewsets

from orc.datamodel.models import VerblijfsObject, NietNatuurlijkPersoon

from .serializers import VerblijfsObjectSerializer, \
    NietNatuurlijkPersoonSerializer


class VerblijfsObjectViewSet(viewsets.ModelViewSet):
    queryset = VerblijfsObject.objects.all()
    serializer_class = VerblijfsObjectSerializer


class NietNatuurlijkPersoonViewSet(viewsets.ModelViewSet):
    queryset = NietNatuurlijkPersoon.objects.all()
    serializer_class = NietNatuurlijkPersoonSerializer
