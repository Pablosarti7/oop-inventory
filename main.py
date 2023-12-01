from product import Product
from inventory import Inventory
from cart import Cart
from shop import Shop
from user import User
from authentication import Authentication

product_one = Product('Antigua', 20, 'medium', 'smooth', 'fruity', 12345)
product_two = Product('Antigua', 20, 'medium', 'smooth', 'fruity', 12346)
product_three = Product('Antigua', 20, 'medium', 'smooth', 'fruity', 12347)
product_four = Product('Huehuetenango', 22, 'medium', 'smooth', 'fruity', 12345)

inventory = Inventory()
inventory.add_product(product_one)
inventory.add_product(product_two)
inventory.add_product(product_three)
inventory.add_product(product_four)

user = User()
authentication = Authentication(user)
authentication.register('Pablo Sarti', 'fakemail@gmail.com', '12345')
authentication.register('Pablo Sarti', 'python@gmail.com', '67890')
authentication.login('fakemail@gmail.com', '12345')
authentication.login('python@gmail.com', '67890')


cart = Cart()
shop = Shop(inventory, cart)
shop.add_cart(product_four)
shop.remove_cart(product_four)

shop.store()