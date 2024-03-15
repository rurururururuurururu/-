class Coffee:
    def __init__(self, name, price, krepost):
        self.name = name
        self.price = price
        self.krepost  = krepost

    def int_coffee(self):
        print(f"coffee: {self.name}, price: {self.price} rub., krepost: {self.krepost}")

my_coffee = Coffee("Amerikano", 120, "heigh")
my_coffee.int_coffee()