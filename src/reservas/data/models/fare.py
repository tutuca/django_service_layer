from django.conf import settings
from .base import BaseModel, models, serializers


class Fare(BaseModel):
    class FareType(models.TextChoices):
        ST: str = "solo-tren"
        BTB: str = "bus-tren-bus"

    kind = models.CharField(max_length=settings.MAX_CHAR_LENGTH, choices=FareType, default=FareType.BTB)
    available_seats = models.IntegerField(default=0)
    date = models.DateTimeField()

    def __str__(self) -> str:
        date = self.date.strftime(settings.DATETIME_FORMAT)
        return f"{self.available_seats}-{self.kind}-{date}"


class Serializer(serializers.ModelSerializer):
    kind = serializers.ChoiceField(choices=Fare.FareType)
    available_seats = serializers.IntegerField()
    date = serializers.DateTimeField(format=settings.DATETIME_FORMAT)

    class Meta:
        model = Fare
        fields = ["id", "kind", "available_seats", "date"]


Fare.Serializer = Serializer
