# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.kw.zain.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for store in stores:
        print(store.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
