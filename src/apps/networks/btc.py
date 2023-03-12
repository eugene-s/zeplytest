from dataclasses import dataclass

import bip32utils as b23u

from ..wallets.models import Wallet
from .base import NetworkABC
from .types import SupportedNetwork


@dataclass(frozen=True)
class BTCNetwork(NetworkABC):
    network: SupportedNetwork = SupportedNetwork.BTC

    def generate_address(self, wallet: Wallet) -> str:
        root_key = b23u.BIP32Key.fromEntropy(wallet.seed.encode())
        return root_key.Address()
