class Inventory:

    def __init__(self) -> None:
        self.items = {}


    def add_product(self, product):
        if product.name in self.items:
            self.items[product.name].append(product)
        else:
            self.items[product.name] = [product]


    def remove_product(self, obj, sku: int):
        for dict_name in self.items:
            if dict_name == obj.name:
                for item in self.items[dict_name]:
                    if item.sku == sku:
                        self.items[dict_name].remove(item)
                    

    def display_inventory(self):
        print('Welcome to my coffee shop.\nThis are the current coffee bags.\n')
        num = 1
        for dict_key, dict_value in self.items.items():
            print(f'{num}. {dict_key}')
            if len(dict_value) < 3:
                print(f"   Only {len(dict_value)} {dict_key} in stock")
            # for value in dict_value:
            #     print(f"    Product Name: {value.name}, Price: {value.price}, SKU: {value.sku}")
            else:
                continue