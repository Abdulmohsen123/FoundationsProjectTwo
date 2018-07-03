# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        # your code goes here!
        self.name = name
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
        self.products.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        for product in self.products:
            print("Name: {} \n Description: {} \n Price: {}".format(product.name,product.description,product.price))


class Product():
    name = ""
    description = ""
    price = 0.0
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        self.name = name
        self.description = description
        self.price = price
        # your code goes here!
    def __str__(self):
        # your code goes here!
        return ("{} is {} priced at {} KD").format(self.name,self.description,self.price)

class Cart():
    cart_products = []
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!
        self.cart_products = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.cart_products.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        total_price = 0.0
        for product in self.cart_products:
            total_price += product.price
        return total_price

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!
        print("Total Price: {}".format(self.get_total_price))

    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!
        print("Price: {}".format(self.get_total_price()))
