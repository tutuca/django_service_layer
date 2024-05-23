from reservas.data import models
from .base import BasePermissionMixin, viewsets


class Fare(BasePermissionMixin, viewsets.ModelViewSet):
    queryset = models.Fare.objects.all()
    serializer_class = models.Fare.Serializer


class Booking(BasePermissionMixin, viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = models.Booking.Serializer


class Pax(BasePermissionMixin, viewsets.ModelViewSet):
    queryset = models.Pax.objects.all()
    serializer_class = models.Pax.Serializer


class Buyer(BasePermissionMixin, viewsets.ModelViewSet):
    queryset = models.Buyer.objects.all()
    serializer_class = models.Buyer.Serializer
