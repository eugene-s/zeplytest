import factory as f
import xrpl as x

from apps.wallets.backend import DEFAULT_ALGORYTHM
from apps.wallets.models import Wallet


class WalletFactory(f.django.DjangoModelFactory):
    class Meta:
        model = Wallet

    class Params:
        internal_wallet = f.LazyFunction(lambda: x.wallet.Wallet.create(DEFAULT_ALGORYTHM))

    seed = f.SelfAttribute("internal_wallet.seed")
    sequence = f.SelfAttribute("internal_wallet.sequence")
    public_key = f.SelfAttribute("internal_wallet.public_key")
    private_key = f.SelfAttribute("internal_wallet.private_key")
