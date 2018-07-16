from rest_framework import viewsets

from orc.datamodel.models import VerblijfsObject

from .serializers import VerblijfsObjectSerializer


class VerblijfsObjectViewSet(viewsets.ModelViewSet):
    queryset = VerblijfsObject.objects.all()
    serializer_class = VerblijfsObjectSerializer
