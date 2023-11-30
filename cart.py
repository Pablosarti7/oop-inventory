class Cart():

    def __init__(self) -> None:
        self.cart = {}
        self.quantity = 0


    def add_to_cart(self, item):
        if item.name in self.cart:
            self.cart[item.name].append(item)
        else:
            self.cart[item.name] = [item]

        self.quantity += 1
        self.__cart_status()

    
    def remove_from_cart(self, item):
        self.cart[item.name].pop()
        self.quantity -= 1
        self.__cart_status()


    def __cart_status(self):
        for dict_key, dict_value in self.cart.items():
            if self.cart[dict_key]:
                print(f'Name: {dict_key}, Quantity: {len(dict_value)}')
            else:
                print("Cart is empty.")
        print(f'Number of cart items: {self.quantity}\n')
        print(self.__calculate_total())

    # Abstraction
    def __calculate_total(self):
        sub_total = 0
        for dict_key in self.cart:
            for item in self.cart[dict_key]:
                sub_total += item.price

        return f'Cart Total: {sub_total}\n'
    