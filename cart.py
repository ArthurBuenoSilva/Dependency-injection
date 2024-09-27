from typing import List

from product import Product


class ShoppingCart:
    def __init__(self):
        self._products: List[Product] = list()

    @property
    def products(self) -> List[Product]:
        return self._products

    def add_product(self, product: Product):
        """Add a new product to cart

        :param product: A product to be added
        """
        self._products.append(product)

    def remove_product(self, product: Product):
        """Remove a product from cart

        :param product: A product to be removed
        """
        self._products.remove(product)

    def calculate_total(self) -> float:
        """Calculate the cart's total price

        :return: The cart's total price
        """
        return sum(product.price for product in self.products)

    def invoice(self):
        """Show cart's invoice
        """
        print("------------ Invoice ------------")
        for product in self.products:
            print(f"{product.name}: ${product.price:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")
        print("---------------------------------")