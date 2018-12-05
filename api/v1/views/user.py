from rest_framework import viewsets, mixins

from api.v1.filters import IsUserFilterBackend
from api.v1.permissions import IsUser
from api.v1.serializers.user import UserSerializer
from authentication.models import User


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsUser,)
    filter_backends = (IsUserFilterBackend, )
