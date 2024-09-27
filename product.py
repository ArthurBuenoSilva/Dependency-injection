from typing import List

from discount import Discount
from tax import Tax


class Product:
    def __init__(self, name: str, price: float, discounts: List[Discount] = None, taxes: List[Tax] = None):
        self.name = name
        self._price = price
        self.discounts = discounts if discounts is not None else list()
        self.taxes = taxes if taxes is not None else list()

    @property
    def price(self) -> float:
        """Apply discounts and taxes

        :return: Price with discounts and taxes applied
        """
        final_price = self._price
        for discount in self.discounts:
            final_price = discount.apply(final_price)

        for tax in self.taxes:
            final_price = tax.apply(final_price)

        return final_price