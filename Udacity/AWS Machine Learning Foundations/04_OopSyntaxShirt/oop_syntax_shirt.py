from tests import run_tests


class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price, pattern):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price
        self._pattern = pattern

    def get_pattern(self):
        return self._pattern

    def set_pattern(self, new_pattern):
        self._pattern = new_pattern

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)


# TODO:
#    - instantiate a shirt object with the following characteristics:
#        - color red, size S, style long-sleeve, and price 25
#    - store the object in a variable called shirt_one

shirt_one = Shirt('red', 'S', 'long-sleeve', 25, 'rectangles')

# TODO:
#     - print the price of the shirt using the price attribute
#     - use the change_price method to change the price of the shirt to 10
#     - print the price of the shirt using the price attribute
#     - use the discount method to print the price of the shirt with a 12% discount

print(shirt_one.price)
shirt_one.change_price(10)
print(shirt_one.price)
print(shirt_one.discount(0.12))

# TODO:
#    - instantiate another object with the following characteristics:
#        - color orange, size L, style short-sleeve, and price 10
#    - store the object in a variable called shirt_two

shirt_two = Shirt('orange', 'L', 'short-sleeve', 10, 'circles')

# TODO:
#    - calculate the total cost of shirt_one and shirt_two
#    - store the results in a variable called total

total = shirt_one.price + shirt_two.price
print(total)

# TODO:
#    - use the shirt discount method to calculate the total cost if
#       shirt_one has a discount of 14% and shirt_two has a discount
#       of 6%
#    - store the results in a variable called total_discount

total_discount = shirt_one.discount(0.06) + shirt_two.discount(0.14)
print(total_discount)
print(shirt_one.get_pattern())
print(shirt_two.get_pattern())

shirt_two.set_pattern('triangles')
print(shirt_two.get_pattern())

run_tests(shirt_one, shirt_two, total, total_discount)
