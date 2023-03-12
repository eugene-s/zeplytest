import pytest

from apps.addresses.backend import AddressCreator
from apps.networks.types import SupportedNetwork
from tests.apps.wallets.factories import WalletFactory


@pytest.mark.parametrize("network", list(SupportedNetwork))
def test_address_creator(network):
    wallet = WalletFactory.build()
    creator = AddressCreator(wallet)
    assert creator.get_address(network)
