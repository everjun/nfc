from rest_framework import viewsets

from api.v1.filters import IsOwnerFilterBackend
from api.v1.permissions.isowner import IsOwner
from api.v1.serializers import CupSerializer
from coffee.models import Cup


class CupViewSet(viewsets.ModelViewSet):
    serializer_class = CupSerializer
    queryset = Cup.objects.all()
    permission_classes = (IsOwner, )
    filter_backends = (IsOwnerFilterBackend, )

