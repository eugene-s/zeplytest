from django.db import models

import apps.wallets.models as awm
from apps.networks.types import SupportedNetwork


class Address(models.Model):
    wallet = models.ForeignKey(awm.Wallet, models.PROTECT)

    address = models.TextField()
    network = models.TextField(choices=SupportedNetwork.choices)

    class Meta:
        unique_together = (("network", "wallet"),)
