"""
Module containing classes Flower, FlowerShop, and Bouquet.
"""


class Flower:
    """
    Class representing a flower.
    """

    def __init__(self, height, size, color, price, quantity, delivery_rate):
        """
        Initializes an instance of the Flower class.
        """
        self.__height = height
        self.__size = size
        self.__color = color
        self.__price = price
        self.__quantity = quantity
        self.__delivery_rate = delivery_rate

    def get_quantity(self):
        """
        Returns the quantity of flowers.
        """
        return self.__quantity

    def get_price(self):
        """
        Returns the price of the flowers.
        """
        return self.__price

    def __str__(self):
        """
        Returns a string with the description of the flower.
        """
        return (f'Desc: Height is {self.__height}cm. Size is {self.__size}. '
                f'Color is {self.__color}.\n Price: {self.__price} usd. '
                f'Quantity is {self.__quantity}. Delivery rate is {self.__delivery_rate}')

    def __repr__(self):
        """
        Returns a string representation of the Flower object.
        """
        return (f'Flower({self.__height}, {self.__size}, {self.__color},'
                f' {self.__price}, {self.__quantity}, {self.__delivery_rate})')


class FlowerShop:
    """
    Class representing a flower shop.
    """

    def __init__(self):
        """
        Initializes an instance of the FlowerShop class.
        """
        self.flowers = {}

    def get_flowers(self):
        """
        Outputs information about the flowers in the shop.
        """
        result = ""
        for name, flower in self.flowers.items():
            result += f"Flower {name}: {flower}\n"
        return result

    def add_flower(self, name, flower, quantity):
        """
        Adds a flower to the shop with the specified quantity.
        """
        if 0 < quantity <= flower.get_quantity():
            self.flowers[name] = {
                'flower': name,
                'quantity': quantity,
                'price': flower.get_price()
            }
        elif quantity <= 0:
            print(f'Cannot add less than 0 {name} flowers.')
        else:
            print(f'Cannot add more than {flower.get_quantity()} {name} flowers.')

    def remove_flower(self, name):
        """
        Removes a flower from the shop by name.
        """
        if name in self.flowers:
            del self.flowers[name]
        else:
            print(f'{name} is not available in the shop.')

    def top_flowers(self):
        """
        Outputs the top 3 flowers by price.
        """
        sorted_flowers = sorted(self.flowers.values(), key=lambda x: x['price'], reverse=True)
        top_three = sorted_flowers[:3]

        result = "Top 3 flowers by price:\n"
        for i, flower in enumerate(top_three):
            result += f"{i + 1}. {flower['flower']} --- Price: {flower['price']}usd.\n"
        return result

    def __str__(self):
        """
        Returns a string with the inventory of the flower shop.
        """
        flower_shop_str = "Flower Shop Inventory:\n"
        for flower in self.flowers.values():
            flower_shop_str += (f"{flower['flower']} - Quantity: {flower['quantity']}, "
                                f"Price: {flower['price']}\n")
        return flower_shop_str


class Bouquet(FlowerShop):
    """
    Class representing a bouquet, which is a subclass of FlowerShop.
    """

    def total_price(self):
        """
        Outputs the total price of the bouquet.
        """
        total_price = sum(flower['price'] * flower['quantity'] for flower in self.flowers.values())
        return total_price


rose = Flower(12, "small", "red", 60, 7, 10)
romashka = Flower(18, "middle", "white", 50, 4, 8)
tulpan = Flower(10, "high", "pink", 30, 1, 9)
store = FlowerShop()
bouquet = Bouquet()

store.add_flower('romashka', romashka, 1)
store.add_flower('rose', rose, 7)
store.add_flower('tulpan', tulpan, 1)
print(store.get_flowers())
store.top_flowers()

bouquet.add_flower('romashka', romashka, 1)
bouquet.add_flower('rose', rose, 7)
bouquet.add_flower('tulpan', tulpan, 1)
bouquet.get_flowers()
bouquet.total_price()
