from rest_framework import viewsets

from orc.datamodel.models import DomeinData

from .serializers import DomeinDataSerializer


class DomeinDataViewSet(viewsets.ModelViewSet):
    queryset = DomeinData.objects.all()
    serializer_class = DomeinDataSerializer
