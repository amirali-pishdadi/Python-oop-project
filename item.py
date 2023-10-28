import csv


class Item:
    pay_rate = 0.4  # user should pay 0.6
    all = []

    def __init__(self, name: str, price: float, quantity: int = 0):
        # Errors
        assert price >= 0, f"Price {price} is not greater or equal to 0 !"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to 0 !"
        # set self values
        self.__name = name
        self.__price = price
        self.__quantity = quantity

        #
        Item.all.append(self)

    def apply_discount(self):
        self.__price = self.__price - (self.__price * self.pay_rate)

    def calculate_total_price(self):
        return self.__price * self.__quantity

    @classmethod
    def read_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(item.get("name"), float(item.get("price")),
                 int(item.get("quantity")))

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self , value):
        if len(value) > 10 :
            raise Exception("The name is too long !")
        else:
            self.__name = value

    def __repr__ (self):
        return f"{self.__class__.__name__}('{self.name}' , {self.price} , {self.quantity})"
