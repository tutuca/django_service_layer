from django.conf import settings
from .base import BaseModel, models, serializers


class Buyer(BaseModel):
    name = models.CharField(
        max_length=settings.MAX_CHAR_LENGTH,
    )
    booking = models.CharField(
        max_length=settings.MAX_CHAR_LENGTH,
    )

    class Serializer(serializers.Serializer):
        name = serializers.CharField()
        booking = serializers.CharField()
