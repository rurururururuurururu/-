
class Kvartira:
    def __init__(self, area, num):
        self.area = area
        self.num_rooms = num

    def calculate(self, rent_price_m):
        total_rent = self.area * rent_price_m
        return total_rent


kvartira = Kvartira(100, 67)


rent_price_m = 100000000
total_cost = kvartira.calculate(rent_price_m)
print(f"стоимость арендквартиры: {total_cost} руб.")