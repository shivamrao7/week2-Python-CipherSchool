class Laptop:
    def __init__(self, name,brand,price):
        self.name = name
        self.brand = brand
        self.price = price
    def full_name(self):
        return f"full name is {self.name} "
    def full_brand(self):
        return f"full name is {self.brand} "
    def full_price(self):
        return f"full name is {self.price} "
    def full_structure(self):
        return f"I am laptop my name is {self.name} and my brand is {self.brand} and my price is {self.price}"

class SmartLaptop(Laptop):
    def __init__(self, name,brand,price,ram,internal_ram, graphic_card):
        super().__init__(name,brand,price)
        self.ram = ram
        self.internal_ram = internal_ram
        self.graphic_card = graphic_card
    

now = Laptop("DELLaspiron","DEll",70000)
now1 = SmartLaptop("MAcbook" ,"applemac",2000000, "2TB","16GB","2TB")
# print(now.full_name())
print(now1.full_name())
print(now.full_structure())
print(now1.full_structure())




