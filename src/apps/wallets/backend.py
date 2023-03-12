import xrpl as x
from xrpl import CryptoAlgorithm

DEFAULT_ALGORYTHM = CryptoAlgorithm.ED25519


def create_wallet() -> x.wallet.Wallet:
    # better to use own wallet instead of Ripple else as it should be to our project related
    return x.wallet.Wallet.create(DEFAULT_ALGORYTHM)
