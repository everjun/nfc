from rest_framework import viewsets, mixins
from rest_framework.response import Response

from api.v1.serializers import PaySerializer
from coffee.models import Cup


class ChangeMoneyViewSet(mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = PaySerializer
    queryset = Cup.objects.none()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.save()
        return Response({'status': 'OK'})
