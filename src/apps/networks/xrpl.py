from dataclasses import dataclass, field

import xrpl as x
from django.conf import settings

from apps.addresses.models import Address

from ..wallets.backend import DEFAULT_ALGORYTHM
from ..wallets.models import Wallet
from .base import NetworkABC
from .types import SupportedNetwork


def default_xrpl_client():
    return x.clients.JsonRpcClient(settings.XRP_LEDGER_URL)


@dataclass(frozen=True)
class XRPLNetwork(NetworkABC):
    client: x.clients.JsonRpcClient = field(default_factory=default_xrpl_client)
    network: SupportedNetwork = SupportedNetwork.XRP

    def generate_address(self, wallet: Wallet) -> str:
        ripple_wallet = x.wallet.Wallet(wallet.seed, wallet.seed, algorithm=DEFAULT_ALGORYTHM)
        return ripple_wallet.classic_address
