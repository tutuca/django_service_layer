from django.conf import settings
from .base import BaseModel, models, serializers


class Pax(BaseModel):
    name = models.CharField(
        max_length=settings.MAX_CHAR_LENGTH,
    )
    booking = models.CharField(
        max_length=settings.MAX_CHAR_LENGTH,
    )
    seat = models.CharField(max_length=settings.MAX_CHAR_LENGTH, default="")

    class Serializer(serializers.Serializer):
        name = serializers.CharField()
        booking = serializers.CharField()
        seat = serializers.CharField()
