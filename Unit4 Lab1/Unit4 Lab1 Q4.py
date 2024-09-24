class Product:

    def __init__(self, code, name, price, quantity):
        self.__product_code = code
        self.__product_name = name
        self.__product_price = price
        self.__product_quantity = quantity

    def get_product_price(self):
        return self.__product_price

    def get_product_quantity(self):
        return self.__product_quantity

    def set_product_price(self, newPrice):
        self.__product_price = newPrice

    def set_product_quantity(self, newQuanity):
        self.__product_quantity = newQuanity 

    def calc_product_value(self):
        return self.__product_price * self.__product_quantity

    def __str__(self):
        return f"   {self.__product_code} : " + format(self.__product_name, "<20s") +  format(self.get_product_quantity(), ">7,d") + " Units @ " + format(self.get_product_price(), ">10,.2f") + " = $" + format(self.calc_product_value(), ",.2f")

product1 = Product(1, "Widget", 21.50, 233)
product2 = Product(2, "Thingamabob ", 750.00, 25)
print(product1)
print(product2)
product1.set_product_price(product1.get_product_price() * 1.30)
print("Price Increase")
print(product1)
product2.set_product_quantity(product2.get_product_quantity() + 1000)
print("New Inventory")
print(product2)