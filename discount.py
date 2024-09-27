from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def apply(self, price: float) -> float:
        """Apply a discount to a product

        :param price: Product's price
        :return: Returns the price with discount applied
        """
        pass


class PercentageDiscount(Discount):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply(self, price: float) -> float:
        return price - (price * self.percentage / 100)


class FixedDiscount(Discount):
    def __init__(self, discount: float):
        self.discount = discount

    def apply(self, price: float) -> float:
        return price - self.discount