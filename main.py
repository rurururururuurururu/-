class Fruit:
    def __init__(self, name, price_per_kg):
        self.name = name
        self.price_per_kg = price_per_kg
    def calculate_cost(self, weight):
        total_cost = self.price_per_kg * weight
        return total_cost
apple = Fruit("Яблоки", 100)
banana = Fruit("Бананчики", 150)


weight1 = 2
cost1 = apple.calculate_cost(weight1)
print(f"Стоимость {weight1} кг яблок: {cost1} руб.")
weight2 = 8
cost2 = banana.calculate_cost(weight2)
print(f"Стоимость {weight2} кг бананочиков: {cost2} руб.")
