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
    for store in stores:
        if store_name == store.name:
            return store
        else:
            print("Sorry we don't have that store")
            return

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    user_input = input("Pick one of our stores: ")
    return get_store(user_input)

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    picked_store.print_products()
    user_picked_product = input("what would you like to buy ?\n")
    
    while user_picked_product != "checkout":
        product_found = False
        for product in picked_store.products:
            if user_picked_product.lower() == product.name.lower():
                print("product found")
                cart.add_to_cart(product)
                product_found = True
        if product_found:
            user_picked_product = input("What else?")
            #if user_picked_product.lower() == "Checkout":
            #product_found = False
        else:
            print("Product not found")
            user_picked_product = input("Please pick a valid product \n")
        
    

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    print_stores()
    store = pick_store()
    pick_products(cart,store)
    cart.checkout()

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
