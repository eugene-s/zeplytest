from dataclasses import dataclass

import sha3

from ..wallets.models import Wallet
from .base import NetworkABC
from .types import SupportedNetwork


@dataclass(frozen=True)
class ETHNetwork(NetworkABC):
    network: SupportedNetwork = SupportedNetwork.ETH

    def generate_address(self, wallet: Wallet) -> str:
        address = sha3.keccak_256(wallet.public_key.encode()).digest()[-20:]
        return f"0x{address.hex()}"
