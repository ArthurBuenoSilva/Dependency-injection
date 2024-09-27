from cart import ShoppingCart
from discount import PercentageDiscount, FixedDiscount
from product import Product
from tax import PercentageTax, FixedTax

if __name__ == '__main__':
    # Creating discounts
    five_percent_discount = PercentageDiscount(5)
    ten_percent_discount = PercentageDiscount(10)
    two_dollars_discount = FixedDiscount(2)

    # Creating taxes
    state_tax = PercentageTax(6)
    federal_tax = PercentageTax(12)
    electronic_tax = FixedTax(8)

    # Creating products
    apple = Product("apple", 0.85, taxes=[state_tax])
    fridge = Product("fridge", 120, [ten_percent_discount], [state_tax, electronic_tax])
    monster_energy = Product("monster_energy", 8, [two_dollars_discount], [federal_tax])
    frozen_pizza = Product(
        "frozen_pizza",
        13,
        [ten_percent_discount, two_dollars_discount]
    )

    # Adding Products to cart
    cart = ShoppingCart()
    cart.add_product(apple)
    cart.add_product(fridge)
    cart.add_product(monster_energy)
    cart.add_product(frozen_pizza)

    cart.invoice()