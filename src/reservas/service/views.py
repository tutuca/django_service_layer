from rest_framework import viewsets

from reservas.data import models


class Fare(viewsets.ModelViewSet):
    queryset = models.Fare.objects.all()
    serializer_class = models.Fare.Serializer


class Booking(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = models.Booking.Serializer


class Pax(viewsets.ModelViewSet):
    queryset = models.Pax.objects.all()
    serializer_class = models.Pax.Serializer


class Buyer(viewsets.ModelViewSet):
    queryset = models.Buyer.objects.all()
    serializer_class = models.Buyer.Serializer


VIEWS = [
    (r"fare", Fare),
    (r"bookings", Booking),
    (r"pax", Pax),
    (r"buyer", Buyer),
]
