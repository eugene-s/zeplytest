from typing import Final

from .base import NetworkABC
from .btc import BTCNetwork
from .eth import ETHNetwork
from .types import SupportedNetwork
from .xrpl import XRPLNetwork

network_registry: Final[dict[SupportedNetwork, type[NetworkABC]]] = {
    SupportedNetwork.BTC: BTCNetwork,
    SupportedNetwork.ETH: ETHNetwork,
    SupportedNetwork.XRP: XRPLNetwork,
}


def get_network(network: SupportedNetwork) -> NetworkABC:
    return network_registry[network]()
