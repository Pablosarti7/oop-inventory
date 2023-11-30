class Shop():
    
    def __init__(self, inventory, cart):
        self.inventory = inventory
        self.cart = cart


    def store(self):
        self.inventory.display_inventory()


    def add_cart(self, product):
        self.cart.add_to_cart(product)
        self.inventory.remove_product(product, product.sku)


    def remove_cart(self, product):
        self.cart.remove_from_cart(product)
        self.inventory.add_product(product)
