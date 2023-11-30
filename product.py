class Product:

    discount = 0.5

    def __init__(self, name, price, roast, texture, taste_profile, sku: int) -> None:
        assert price >= 0, f'Price {price} is not greater or equal to zero'
        # assert quantity >= 0, f'Quantity {quantity} is not greater or equal ro zero'

        self.__name = name
        self.price = price 
        self.roast = roast
        self.texture = texture
        self.taste_profile = taste_profile
        self.sku = sku
        # self.quantity = quantity

    # Encapsulation
    @property
    def name(self):
        return self.__name

    def apply_discount(self):
        self.price = self.price * Product.discount
        

# add quantity parameter but also modify inventory management