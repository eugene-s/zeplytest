import pytest

from apps.wallets.models import Wallet
from apps.wallets.serializers import WalletCreateSerializer


@pytest.mark.django_db
def test_create_wallet_serializer():
    serializer = WalletCreateSerializer(data={})
    assert serializer.is_valid()
    assert serializer.save()
    assert Wallet.objects.count() == 1
