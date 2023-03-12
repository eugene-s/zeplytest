from rest_framework import serializers as s
from rest_framework import validators as _v

from .backend import AddressCreator
from .models import Address


class AddressSerializer(s.ModelSerializer):
    class Meta:
        model = Address
        fields = ("address", "network")


class AddressCreateSerializer(s.ModelSerializer):
    class Meta:
        model = Address
        fields = ("network", "wallet")
        validators = (
            _v.UniqueTogetherValidator(
                queryset=Address.objects.all(),
                fields=("network", "wallet"),
                message="This wallet already has the address for the selected network.",
            ),
        )

    def save(self, **kwargs):
        # todo: get wallet from an authorized user
        data = self.validated_data
        creator = AddressCreator(data["wallet"])
        address = creator.get_address(data["network"])
        return super().save(address=address, **kwargs)
