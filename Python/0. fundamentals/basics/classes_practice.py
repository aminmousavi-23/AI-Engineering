class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self._price = price
        self.__quantity = quantity
        self.made_in = "USA"

    def display_info(self):
        print(f"{self.name} : price = {self._price}, quantity = {self.__quantity}")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price

    @property
    def quantity(self):
        return self.__quantity


p1 = Product("Iphone 17 pro", 969.00, 30)

p1.display_info()


class Car(Product):
    def __init__(self, name, price, quantity, brand):
        super().__init__(name, price, quantity)
        self.brand = brand

    def display_info(self):
        print(f"{self.name} : price = {self.price}, quantity = {self.quantity}, brand = {self.brand}")


c1 = Car("C 200", 16000.00, 12, "Mercedes Benz")

c1.display_info()

