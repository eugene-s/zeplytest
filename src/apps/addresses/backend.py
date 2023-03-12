from dataclasses import dataclass

from apps.networks.adapter import get_network
from apps.networks.types import SupportedNetwork
from apps.wallets.models import Wallet


@dataclass(frozen=True)
class AddressCreator:
    wallet: Wallet

    def get_address(self, network: SupportedNetwork) -> str:
        manager = get_network(network)
        return manager.generate_address(self.wallet)
