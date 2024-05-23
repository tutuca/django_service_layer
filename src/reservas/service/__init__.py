from rest_framework import viewsets, serializers


def viewset_factory(model, queryset=None, authorization_classes=None):
    _queryset = model.objects.all() if queryset is None else queryset
    _authorization_classes = authorization_classes
    _serializer_class = getattr(model, "Serializer", serializers.ModelSerializer)

    class Viewset(viewsets.ModelViewSet):
        serializer_class = _serializer_class
        queryset = _queryset
        authorization_classes = _authorization_classes

    return Viewset
