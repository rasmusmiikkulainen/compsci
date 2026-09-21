class Product:
    current_id = 0 # class attribute
    def __init__(self, description, price): # instance method
        self.description = description
        self.id_num = Product.current_id
        Product.current_id += 1
        self.price = price
    def __str__(self):
        return f"product {self.description}, id {self.id_num} @ {self.price}"

ps = [Product("thinkpad", 1299.95), Product("mac", 3299.95)] # __init__() called behind scenes
for p in ps:
    print(p) # __str__() called behind scenes
print(Product.mro())