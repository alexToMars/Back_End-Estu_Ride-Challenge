from rest_framework import routers
from .api import ReservationViewSet

router = routers.DefaultRouter()

router.register('api/reservations',ReservationViewSet,'reservations')

urlpatterns=router.urls