from rest_framework.routers import DefaultRouter

from api.v1.views import CupViewSet, ChangeMoneyViewSet
from api.v1.views.user import UserViewSet

router = DefaultRouter()
router.register('cup', CupViewSet)
router.register('user', UserViewSet)
router.register('pay', ChangeMoneyViewSet)


urlpatterns = router.urls
