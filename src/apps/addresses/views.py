from rest_framework import mixins as _m
from rest_framework import viewsets as _v

from .models import Address
from .serializers import AddressCreateSerializer, AddressListSerializer, AddressSerializer

__all__ = ("AddressViewSet",)


class AddressViewSet(
    _m.ListModelMixin,
    _m.CreateModelMixin,
    _m.RetrieveModelMixin,
    _v.GenericViewSet,
):
    queryset = Address.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return AddressCreateSerializer
        if self.action == "list":
            return AddressListSerializer
        return AddressSerializer
