import random
import string

from django.conf import settings

from .base import BaseModel, models, serializers


def build_booking_code():
    code = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    return code


class Booking(BaseModel):
    fare = models.ForeignKey("data.Fare", on_delete=models.CASCADE)
    code = models.CharField(max_length=settings.MAX_CHAR_LENGTH, default=build_booking_code)

    def __str__(self) -> str:
        return f"{self.fare.kind}-{self.code}"


class Serializer(serializers.ModelSerializer):
    fare = serializers.CharField(source="fare.kind")
    code = serializers.CharField()

    class Meta:
        model = Booking
        fields = ["fare", "code"]


Booking.Serializer = Serializer
