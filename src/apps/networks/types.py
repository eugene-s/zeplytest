from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class SupportedNetwork(TextChoices):
    BTC = "BTC", _("BTC")
    ETH = "ETH", _("ETH")
    XRP = "XRP", _("XRP")
