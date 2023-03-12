import pytest

from apps.addresses.serializers import AddressCreateSerializer
from apps.networks.types import SupportedNetwork
from tests.apps.wallets.factories import WalletFactory


@pytest.mark.django_db
@pytest.mark.parametrize("network", list(SupportedNetwork))
def test_create_address_serializer(network):
    wallet = WalletFactory()
    serializer = AddressCreateSerializer(
        data={
            "wallet": wallet.pk,
            "network": network,
        }
    )
    assert serializer.is_valid()
