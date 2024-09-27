from abc import ABC, abstractmethod


class Tax(ABC):
    @abstractmethod
    def apply(self, price: float) -> float:
        """Apply a tax to a product

        :param price: Product's price
        :return: Returns the price with tax applied
        """
        pass


class PercentageTax(Tax):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply(self, price: float) -> float:
        return price + (price * self.percentage / 100)


class FixedTax(Tax):
    def __init__(self, tax: float):
        self.tax = tax

    def apply(self, price: float) -> float:
        return price + self.tax