import factory as f
import factory.fuzzy

from apps.addresses.backend import AddressCreator
from apps.networks.types import SupportedNetwork


class AddressFactory(f.django.DjangoModelFactory):
    wallet = f.SubFactory("tests.apps.wallets.factory.WalletFactory")
    network = f.fuzzy.FuzzyChoice(list(SupportedNetwork))
    address = f.LazyAttribute(lambda self: AddressCreator(self.wallet).get_address(self.network))
