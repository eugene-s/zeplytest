import abc
from dataclasses import dataclass

from apps.addresses.models import Address
from apps.networks.types import SupportedNetwork
from apps.wallets.models import Wallet


@dataclass(frozen=True)
class NetworkABC(abc.ABC):
    @property
    @abc.abstractmethod
    def network(self) -> SupportedNetwork:
        pass

    @abc.abstractmethod
    def generate_address(self, wallet: Wallet) -> str:
        pass
