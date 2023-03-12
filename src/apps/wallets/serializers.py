from rest_framework import serializers as s

from .backend import create_wallet
from .models import Wallet


class WalletSerializer(s.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("pk",)


class WalletCreateSerializer(s.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("pk",)

    def create(self, validated_data):
        wallet = create_wallet()
        return Wallet.objects.create(
            seed=wallet.seed,
            sequence=wallet.sequence,
            public_key=wallet.public_key,
            private_key=wallet.private_key,
        )
