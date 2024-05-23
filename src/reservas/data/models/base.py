from django.db import models
from rest_framework import serializers


class BaseModel(models.Model):

    class Meta:
        abstract = True

    class Serializer(serializers.Serializer):
        ...

    def serialize(self):
        return self.Serializer(instance=self).data
