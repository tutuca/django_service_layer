from .base import BasePermissionMixin, viewsets
from reservas.data import models


class User(BasePermissionMixin, viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = models.User.Serializer
