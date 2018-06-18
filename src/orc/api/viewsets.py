from rest_framework import viewsets

from orc.datamodel.models import DomeinData, VerblijfsObject

from .serializers import DomeinDataSerializer, VerblijfsObjectSerializer


class DomeinDataViewSet(viewsets.ModelViewSet):
    queryset = DomeinData.objects.all()
    serializer_class = DomeinDataSerializer


class VerblijfsObjectViewSet(viewsets.ModelViewSet):
    queryset = VerblijfsObject.objects.all()
    serializer_class = VerblijfsObjectSerializer
