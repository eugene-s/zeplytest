from rest_framework import mixins as _m
from rest_framework import viewsets as _v

__all__ = ("WalletViewSet",)

from .models import Wallet
from .serializers import WalletCreateSerializer, WalletSerializer


class WalletViewSet(
    _m.CreateModelMixin,
    _m.ListModelMixin,
    _v.GenericViewSet,
):
    queryset = Wallet.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return WalletCreateSerializer
        return WalletSerializer
